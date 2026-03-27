# Developing a Domain-Specific LLM through Self-Instruct Fine-Tuning: Application to Reliability Engineering

**Authors:** Alex Dalban, Elora Drouilhet
**Supervisors:** Dr. Zhiguo Zeng, Jean Meunier-Pion (PhD Candidate)
**Institution:** LGI, CentraleSupelec, Universite Paris-Saclay
**Status:** Work in progress

---

## 1. Introduction and Motivation

Reliability engineering deals with the risk and safety of complex systems such as nuclear power plants, aircraft, and electrical grids. Assessing reliability requires advanced mathematical modeling --- Weibull distributions, Markov chains, Bayesian inference, fault tree analysis --- and extensive domain expertise. General-purpose LLMs, despite their strong performance on standard programming and reasoning benchmarks, perform poorly on reliability-specific tasks. Prior work at CentraleSupelec established an evaluation baseline of ~50 hand-written reliability coding questions and found that state-of-the-art LLMs frequently produced incorrect or nonsensical solutions, failing to grasp domain-specific nuances and multi-step mathematical reasoning (mid-defence slides, December 2025).

This project aims to bridge this gap by fine-tuning open-weight LLMs on synthetically generated, domain-specific training data using an adaptation of the Self-Instruct framework (Wang et al., 2023). The approach has three components: (1) synthetic data generation with chain-of-thought reasoning, (2) quality filtering via cross-model answer consistency, and (3) LoRA-based fine-tuning with rigorous 5-fold cross-validation.

---

## 2. Related Work

### 2.1 Self-Instruct (Wang et al., 2023)

Self-Instruct is a framework for improving instruction-following capabilities of LLMs by bootstrapping off their own generations. Starting from 175 human-written seed tasks, the method uses vanilla GPT-3 (175B) to iteratively generate new instructions, classify them, create input-output instances, and filter low-quality examples via ROUGE-L similarity thresholds (< 0.7). The resulting 52K instructions are used to fine-tune the same GPT-3 model, achieving +33.1% improvement on Super-NaturalInstructions and near-parity with InstructGPT-001.

A critical design choice: **the same model both generates the data and is fine-tuned on it.** This assumes the model has sufficient latent knowledge to produce valid training examples but lacks the alignment to follow instructions reliably. Human evaluation found only 54% of generated examples were fully valid (instruction + input + output all correct), with output quality being the weakest link.

### 2.2 Chain-of-Thought Self-Instruct (Yu et al., 2024)

CoT-Self-Instruct extends the framework by incorporating step-by-step reasoning during generation and using answer-consistency filtering for verifiable tasks. This is directly relevant to our domain, where numerical answers can be objectively verified.

### 2.3 Auto-CoT (Zhang et al., 2022)

Eliminates manual effort in creating chain-of-thought demonstrations by clustering questions by similarity and generating reasoning chains automatically. Relevant for our reasoning generation pipeline.

### 2.4 Self-Refine Instruction Tuning (Ranaldi & Freitas, 2024)

A two-stage approach: (1) instruction-tuning on reasoning demonstrations, then (2) self-refinement through Direct Preference Optimization (DPO). Demonstrates that preference optimization can improve reasoning quality without separate reward models.

### 2.5 Data Augmentation with LLMs (Ding et al., 2024)

Comprehensive survey on using LLMs for data augmentation. Key findings relevant to our work: larger models yield better data, but filtering helps achieve similar results from smaller models; cross-model validation reduces self-reinforcing biases.

---

## 3. Data Pipeline

### 3.1 Phase 1: Textbook Extraction (Seed Dataset)

**Source material.** Reliability engineering textbooks were digitized via OCR (Mistral OCR) into markdown files (32 chapters, stored in `ocr_output/`). These textbooks cover standard reliability topics: exponential, Weibull, and lognormal lifetime distributions; MTTF and hazard functions; Bayesian inference; system reliability (series, parallel, k-out-of-n); reliability demonstration testing; and acceptance sampling.

**Extraction pipeline.** A three-step process:
1. **Keyword scanning:** Regex patterns identify exercise/problem/solution blocks in the OCR output.
2. **LLM-assisted validation:** A language model checks each candidate for self-containment (no references to figures, tables, or prior parts), clear problem formulation, and unambiguous numerical answers.
3. **Structured extraction:** Each validated item is separated into three components: question (q), reasoning (r), and answer (a).

**Iterative refinement.** The seed dataset went through multiple cleaning iterations:
- `raw_extraction_v1.json` (56 items) -> `raw_extraction_v3.json` (cleaned)
- Unicode and LaTeX fixing via LLM-assisted processing (`fix_unicode_latex_llm.ipynb`)
- Manual curation to `seed_dataset.json` (56 items) -> `seed_extended.jsonl` (66 items) -> `seed_latex_cleaned.jsonl` (63 items) -> `seed_subset_49.jsonl` (49 high-quality items)

**Result:** 288 seed (q, r, a) triplets after extraction and validation, covering both exercise-based (numerical) and theory-based (conceptual/MCQ) question types.

### 3.2 Phase 2: Synthetic Data Generation

#### 3.2.1 Adaptation of Self-Instruct

Our approach departs from the original Self-Instruct framework in several significant ways, motivated by the unique challenges of domain-specific mathematical question generation.

**Departure 1: Stronger generator model.** In the original Self-Instruct, vanilla GPT-3 generates data that is then used to fine-tune the same GPT-3. We instead use a **stronger model** (Claude Sonnet 4/4.5 via OpenRouter) to generate questions, while fine-tuning a **smaller model** (Qwen3-8B or Llama 3.1 8B). This is a deliberate choice: our target domain requires precise mathematical reasoning that smaller models struggle with, and we need the generator to produce problems beyond the target model's current capabilities.

**Departure 2: Full chain-of-thought generation.** Each generated example includes not just a question and answer, but a complete step-by-step reasoning chain. The generation prompt explicitly requests "COMPLETE solutions with step-by-step reasoning," producing (q, r, a) triplets rather than simple (instruction, output) pairs. This teaches the fine-tuned model *how to reason*, not just *what to answer*.

**Departure 3: Cross-model answer verification instead of ROUGE-L filtering.** The original Self-Instruct uses ROUGE-L similarity to filter duplicate instructions. This is insufficient for mathematical domains where two very differently-worded questions can have identical solution methods, and where output correctness matters far more than output diversity. We replace this with a **cross-model verification** pipeline (Section 3.3) that independently verifies the correctness of each generated answer.

**Departure 4: Domain-grounded seed pool.** Rather than general-purpose seed tasks, our seed pool consists of textbook-extracted reliability engineering problems. The generation prompt shows 3 randomly sampled seed examples and asks for 2 new problems "inspired by these examples" but with "DIFFERENT questions" using "similar concepts but NEW scenarios."

#### 3.2.2 Generation Process

**Configuration:**
- Generator model: `anthropic/claude-sonnet-4` (later `claude-sonnet-4.5`)
- Temperature: 0.8 (encourages diversity)
- Seed examples per prompt: 3 (randomly sampled from growing pool)
- Questions per batch: 2
- Max tokens: 25,000
- Parallel workers: 5

**Generation prompt** (key instructions):
```
You are an expert in reliability engineering, creating practice problems for students.
[...] Create {n} NEW, ORIGINAL problems that are SIMILAR in style and difficulty [...]
IMPORTANT:
- Create DIFFERENT questions (don't just change numbers in the examples)
- Use similar concepts but NEW scenarios
- Include all necessary data in the question (self-contained)
- Show clear reasoning steps
- Provide specific numerical answers when appropriate
```

**Quality gates at generation time:**
- Minimum question length: 30 characters
- Minimum reasoning length: 50 characters
- Minimum answer length: 1 character
- Placeholder pattern rejection: `[insert`, `tbd`, `to be determined`, `xxx`, `???`
- Deduplication by 200-character question prefix (case-insensitive)

**First generation run:** 81 synthetic questions passed consistency filtering out of an initial larger set (consistency threshold of 50%).

**Second generation run (cross-model):** Extended to 200 target items using the cross-model verification pipeline described in Section 3.3. The seed pool grew iteratively: verified synthetic examples were added back to the pool for subsequent generation rounds (self-instruct bootstrapping).

### 3.3 Phase 3: Cross-Model Answer Verification

A central challenge with synthetic data for mathematical domains is **answer correctness**. Unlike general instruction-following tasks where plausible outputs suffice, reliability engineering demands numerical precision. A generated answer of 0.95 when the correct answer is 0.0385 is unambiguously wrong, regardless of how reasonable the reasoning appears.

**Verification pipeline:**
1. **Generate:** Claude Sonnet 4.5 produces a (q, r, a) triplet from seed examples.
2. **Independent solve:** Claude Opus 4 independently solves the same question (temperature=0.1 for deterministic output, `reasoning_effort="low"`, max_tokens=16384).
3. **Answer extraction:** Gemini 2.5 Flash extracts the final numerical answer from both the generator's and verifier's responses, using pattern matching for "final answer," "therefore," "result."
4. **Hybrid comparison:**
   - **Numerical first:** Extract all numbers via regex from both answers. If both sides yield the same count, compare pairwise with 5% relative tolerance.
   - **LLM fallback:** If numerical comparison is inconclusive (non-numeric, different value counts), Gemini 2.5 Flash performs semantic comparison, outputting "MATCH" or "MISMATCH."
5. **Accept/reject:** Only MATCH items are added to the master dataset.

**Safety valve:** If the acceptance rate drops below 10% after 20 batches, generation halts (indicates systematic quality issues).

**Result:** The combined dataset after cross-model verification: `master_dataset.jsonl` (140 items).

### 3.4 Phase 4: Dataset Cleaning and Finalization

The 140-item master dataset underwent LLM-assisted cleaning (Claude Opus 4.6, temperature=0.1):

1. **Classification:** Each question classified as MULTI_PART_NUMERIC, SINGLE_NUMERIC, FORMULA, DERIVATION, or CONCEPTUAL.
2. **Multi-part splitting:** Questions with sub-parts (a, b, c...) were split into fully self-contained single-answer entries. Each sub-question was rewritten to include all necessary context (no references to "Part (a)" or "the previous problem"). 107 items were split into multiple entries.
3. **Answer standardization:** Trailing periods removed; units stripped (hours, failures, FITs); commas removed from numbers; percentages kept as-is; LaTeX cleaned.
4. **Deduplication:** By 200-character question prefix: 173 duplicates removed.
5. **Self-containment verification:** Checked for banned phrases ("from the previous," "as above," "Part (a)"): 0 failures.

**Final dataset:** `master_dataset_cleaned.jsonl` --- **256 items** (215 numeric, 21 formula, 19 text, 1 boolean). Each item has fields: `question`, `reasoning`, `answer`, `answer_type`, `source` (seed or cross_model_verified), `original_index`.

---

## 4. The Self-Instruct Ceiling Effect: A Key Finding

### 4.1 Observation

During baseline evaluation at the mid-defence stage, a striking pattern emerged. When GPT-4-Mini and R1-Distill-Qwen3-14B were evaluated on both seed (textbook-extracted) and synthetic (LLM-generated) questions:

| Model | Seed Questions (288) | Synthetic Questions (81) |
|-------|---------------------|------------------------|
| GPT-4-Mini | 122/288 = **42.4%** | 74/81 = **91.4%** |
| R1-Distill-Qwen3-14B | 100/288 = **34.7%** | 77/81 = **95.1%** |

Synthetic questions had **dramatically higher accuracy** --- models that struggled on real textbook problems could already solve 91-95% of the synthetic ones.

### 4.2 Interpretation

This reveals a fundamental limitation of the self-instruct paradigm applied to domain-specific tasks, one not addressed in the original Self-Instruct paper (Wang et al., 2023):

**The generating model creates questions within its own capability envelope.** When Claude Sonnet generates reliability engineering problems, it produces questions it can solve. These questions are then solvable by other models of similar or greater capability. The generated questions are systematically easier than real textbook problems because they:

1. **Avoid edge cases** the generator doesn't understand (e.g., truncated distributions, competing risks)
2. **Use standard formulations** that match the generator's training distribution
3. **Have clean numerical answers** that don't require iterative methods or lookup tables
4. **Follow predictable patterns** from the seed examples rather than introducing novel problem structures

### 4.3 Implications for Fine-Tuning

This finding has direct implications for the effectiveness of SFT:

1. **Training on easy questions doesn't teach hard ones.** If the fine-tuning dataset consists primarily of questions the base model can already solve, the model learns format and style but not new capabilities.
2. **The original Self-Instruct sidesteps this problem** because it targets *instruction following* (a capability gap even for knowledgeable models), not *domain knowledge acquisition*. GPT-3 has the knowledge to follow instructions but needs alignment; our models lack the domain knowledge itself.
3. **Cross-model verification helps but doesn't fully solve the problem.** Verification ensures answer correctness but cannot increase question difficulty beyond what the generator can produce.
4. **This suggests a different approach may be needed:** rather than generating new questions, the focus should be on ensuring existing textbook questions (which are genuinely hard) have high-quality reasoning chains that teach the solution process.

### 4.4 Contrast with the Literature

The original Self-Instruct paper acknowledges "minimal gains in low-frequency contexts" as a limitation but frames this as a tail-distribution problem. Our finding is more fundamental: in domain-specific settings where the goal is *knowledge transfer* (not instruction alignment), the generating model's knowledge boundary becomes the training data's difficulty ceiling. This aligns with the SearchInstruct approach (arXiv:2509.10708), which argues that Self-Instruct "depends solely on internal knowledge" and proposes grounding in retrieved documents. For mathematical domains, grounding in textbook source material may be essential.

---

## 5. Fine-Tuning Pipeline

### 5.1 Architecture

**Framework:** Unsloth (optimized LoRA implementation for consumer/HPC GPUs)
**Quantization:** 4-bit (QLoRA via bitsandbytes)
**Adapter:** LoRA applied to all attention and MLP projection layers (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`)
**Hardware:** NVIDIA A100-SXM4-40GB (LaRuche HPC cluster, Universite Paris-Saclay)

### 5.2 Evaluation Protocol

**5-fold cross-validation** on the 215 numeric-only questions (later experiments; initial runs used all 256). Each fold: 172 train / 43 test. The same base model is evaluated before (baseline) and after (fine-tuned) LoRA training on each fold's training set.

**Answer comparison** (`compare_answers`):
- **Exact match:** Normalized strings (lowercased, whitespace removed, LaTeX stripped)
- **Numerical match:** All numbers extracted via regex; pairwise comparison within 5% relative tolerance
- **Fraction-to-decimal:** `14/33` matches `0.4242` (added after initial run to fix false negatives)
- **Percentage conversion:** `25.5%` converted to `0.255` before comparison
- **Partial match:** Substring containment (length > 3)
- **Correct = exact OR numerical OR (partial AND length > 3)**

**Statistical test:** Wilcoxon signed-rank test on per-fold accuracies (paired, non-parametric).

**Chat format for SFT training data:**
```json
{"conversations": [
  {"role": "system", "content": "You are an expert in reliability engineering..."},
  {"role": "user", "content": "<question>"},
  {"role": "assistant", "content": "<reasoning>\n\nFinal Answer: <answer>"}
]}
```

### 5.3 Training Data Format

The `formatting_func` in `train_sft.py` uses `tokenizer.apply_chat_template()` to convert conversations into model-specific token sequences. This makes the pipeline model-agnostic --- the same code works for Llama, Qwen, Gemma, or any model with a HuggingFace chat template.

---

## 6. Experiments and Results

### 6.1 Experiment 0: Mid-Defence Baseline (December 2025)

**Model:** Qwen3-14B (full precision, not quantized)
**Dataset:** 230 train / 58 test (single split, not cross-validated)
**Training:** LoRA fine-tuning (details not recorded in detail)

| Model | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| Unfinetuned Qwen3-14B | 5 | 58 | 8.6% |
| Finetuned Qwen3-14B | 8 | 58 | **13.8%** (+5.2%) |

**Key finding:** Fine-tuning produced a measurable improvement, but accuracy remained very low. The evaluation was on the full question set (including formula and text types) which are harder to score automatically.

### 6.2 Experiment 1: Llama 3.1 8B (5-Fold CV)

**Model:** `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit`
**Dataset:** 256 items (all types), stratified 5-fold CV
**Hyperparameters:** LR=2e-4, 3 epochs, batch=2, grad_accum=4, linear scheduler, lora_r=16, lora_alpha=16, no dropout, max_new_tokens=2048

| Metric | Baseline | Fine-tuned | Delta |
|--------|----------|-----------|-------|
| **Overall accuracy** | 37.5% +/- 3.2% | 39.8% +/- 4.1% | +2.4% |
| Numeric (n=215) | 41.4% | 40.0% | -1.4% |
| Formula (n=21) | 33.3% | **61.9%** | **+28.6%** |
| Text (n=19) | 0.0% | **15.8%** | **+15.8%** |
| Wilcoxon p-value | | | 0.25 (NS) |

**Question flips:** 64 total --- 35 wrong-to-right, 29 right-to-wrong.

**Analysis:** Fine-tuning dramatically improved formula (+28.6pp) and text (+15.8pp) answers, indicating the model learned the expected output format. However, numeric accuracy slightly decreased (-1.4pp), and the overall improvement was not statistically significant. The model gained on structured/formulaic questions but lost on calculation-heavy numerics, suggesting catastrophic forgetting on mathematical capabilities.

### 6.3 Experiment 2: Qwen3-8B, First Run (Thinking Mode, max_tokens=2048)

**Model:** `unsloth/qwen3-8b-unsloth-bnb-4bit`
**Dataset:** 215 numeric-only items, 5-fold CV
**Hyperparameters:** LR=5e-5, 4 epochs, cosine scheduler, lora_r=16, lora_alpha=32, no dropout, max_new_tokens=2048
**Note:** Thinking mode was NOT disabled. The model generated `<think>` blocks during inference.

| Fold | Baseline | Fine-tuned | Delta |
|------|----------|-----------|-------|
| 0 | 65.1% | 62.8% | -2.3% |
| 1 | 74.4% | 76.7% | +2.3% |
| 2 | 62.8% | 69.8% | +7.0% |
| 3 | 60.5% | 60.5% | 0.0% |
| 4 | 76.7% | 65.1% | -11.6% |
| **Mean** | **67.9% +/- 6.5%** | **67.0% +/- 5.8%** | **-0.9%** |
| Wilcoxon p | | | 0.875 (NS) |

**Question flips:** 52 total --- 25 wrong-to-right, 27 right-to-wrong.

**Key findings:**

1. **Qwen3-8B baseline is dramatically stronger than Llama 3.1 8B** (67.9% vs 37.5% on numeric questions), confirming the importance of base model selection for mathematical domains.

2. **Fine-tuning produced no improvement** (-0.9%, p=0.875). Detailed analysis revealed the root cause: **the SFT training data lacked `<think>` blocks**, causing the model to learn to skip its internal reasoning mechanism entirely. All 43 finetuned responses in fold 0 had empty `<think>` blocks (`<think>\n\n</think>`), going straight to a pattern-matched answer.

3. **The baseline's primary failure mode was token truncation**, not reasoning errors. With max_new_tokens=2048, the model's `<think>` blocks were cut off mid-reasoning in 15/15 wrong answers. The model was reasoning correctly but running out of space.

4. **The finetuned model traded reasoning for memorization.** It won on formulaic problems (direct formula application) but lost on multi-step reasoning (Bayes theorem, conditional reliability, k-out-of-n systems). 9.3% of finetuned responses fell into infinite repetition loops.

5. **Finetuned responses were 8x shorter** (mean 679 chars vs 5,489 chars for baseline), confirming the reasoning suppression.

### 6.4 Experiment 3: Qwen3-8B, Round 2 (In Progress)

Based on the analysis of Experiment 2, four simultaneous experiments were designed to address the identified issues. All share these fixes:

**Common changes (applied to all four):**
- `enable_thinking=False` in all `apply_chat_template()` calls --- prevents the thinking-mode mismatch that caused reasoning suppression
- `max_new_tokens=4096` --- prevents truncation
- `lora_dropout=0.05` --- regularization for the small 172-sample training set
- NEFTune noisy embeddings (Jain et al., 2023) --- evidence-backed regularizer that adds uniform noise to embedding vectors during training, shown to produce +25-35% improvements on instruction-following benchmarks
- Cosine learning rate schedule

**Experiment 3a: Best guess (`qwen3-8b-v2`)**
- LR=2e-4, NEFTune alpha=5, lora_r=16, lora_alpha=32, 3 epochs
- Rationale: Research shows optimal LoRA LR is ~10x higher than full fine-tuning LR. Previous run's 5e-5 was likely under-training.

**Experiment 3b: Higher NEFTune (`qwen3-8b-neft10`)**
- Same as 3a but NEFTune alpha=10
- Rationale: Tests sensitivity to embedding noise level. Higher alpha provides stronger regularization against memorization.

**Experiment 3c: Lower rank (`qwen3-8b-lowrank`)**
- LR=2e-4, NEFTune alpha=5, lora_r=8, lora_alpha=16, 3 epochs
- Rationale: Lower LoRA rank acts as implicit regularization, limiting adapter capacity and reducing overfitting risk on 172 training examples.

**Experiment 3d: Lower learning rate (`qwen3-8b-lr1e4`)**
- LR=1e-4, NEFTune alpha=5, lora_r=16, lora_alpha=32, 3 epochs
- Rationale: Tests whether the 2e-4 recommendation holds for our small dataset, or whether a more conservative 1e-4 preserves more base model capability.

**Status:** All four jobs submitted to LaRuche A100 cluster (jobs 429800-429803). First two running, results expected within 6-8 hours of start.

---

## 7. Answer Comparison Improvements

The initial answer comparison function produced false negatives that inflated the right-to-wrong flip count. Three bugs were identified and fixed:

### 7.1 Fraction-to-Decimal Mismatch

**Problem:** Ground truth `"14/33"` and predicted `"0.4242"` were scored as non-matching because the number extractor found `[14, 33]` vs `[0.4242]` --- different counts.

**Fix:** Added `_eval_fraction()` to convert fraction strings to floats before numerical comparison. Now `14/33 = 0.4242...` matches within 5% tolerance.

### 7.2 LaTeX Wrapper Stripping

**Problem:** Predictions like `"$\boxed{\frac{14}{33}}$"` contain LaTeX markup that obscures the actual answer.

**Fix:** `normalize_answer()` now strips `\$\boxed{...}\$`, `\boxed{...}`, `\$...\$`, and converts `\frac{n}{d}` to `n/d`.

### 7.3 Percentage Handling

**Problem:** `"25.5%"` was not matched against `"0.255"`.

**Fix:** Before number extraction, percentages are converted: `25.5%` -> `0.255`.

### 7.4 Single Ground Truth vs Multiple Predictions

**Problem:** A verbose response like "After 10 iterations, the result is 3.5" was compared against ground truth "3.5". Number extraction found `[10, 3.5]` vs `[3.5]` --- different counts, scored as non-matching.

**Fix:** When ground truth has a single number but prediction has multiple, check if *any* predicted number matches within tolerance.

---

## 8. Lessons Learned and Open Questions

### 8.1 What Worked

1. **Cross-model verification** produced a cleaner dataset than self-consistency filtering alone. Using a different model (Claude Opus) to independently solve each generated question catches errors that the generator model would reproduce consistently.

2. **The SFT pipeline infrastructure** (5-fold CV, automated comparison, per-question flip analysis) enabled detailed diagnosis of failure modes that aggregate accuracy numbers would miss.

3. **Model selection matters enormously.** Qwen3-8B achieved 67.9% baseline accuracy vs Llama 3.1 8B's 37.5% on the same numeric questions, a nearly 2x difference with no fine-tuning.

4. **Formula and text questions responded well to SFT** (Llama experiment: +28.6pp on formulas, +15.8pp on text), suggesting the model successfully learned output formatting and structured derivation patterns.

### 8.2 What Didn't Work

1. **SFT on numeric questions showed no improvement** across either model (Llama: -1.4pp, Qwen3: -0.9pp). The questions the model got right changed, but the total count didn't improve.

2. **Thinking-mode models require format-matched training data.** Qwen3-8B's `<think>` mechanism was suppressed by SFT on direct-answer training data, removing the model's ability to reason internally. This is a critical pitfall when fine-tuning reasoning models.

3. **Small datasets (172 training examples) risk catastrophic forgetting.** Even with LoRA (which freezes base weights), the adapter can learn to override correct base model behavior on some questions while helping on others, resulting in a net wash.

4. **Synthetic questions are systematically easier** than real textbook problems (91-95% vs 34-42% baseline accuracy), limiting the training signal available from generated data.

### 8.3 Open Questions

1. **Can we generate harder questions?** Possible approaches: (a) prompt the generator with the hardest seed examples only, (b) use Evol-Instruct (Xu et al., 2023) to iteratively increase complexity, (c) ground generation in textbook source material (SearchInstruct approach).

2. **Would DPO/ORPO work better than SFT?** With 67.9% baseline accuracy, the model already "knows" most of the material. Preference optimization using the model's own correct vs incorrect answers might preserve capabilities while steering behavior.

3. **What is the optimal dataset size?** Literature suggests SFT benefits diminish below ~500 high-quality examples. Our 172 train samples per fold may be below the minimum effective threshold.

4. **Should we fine-tune a non-reasoning model?** The Qwen3-8B thinking-mode mismatch suggests that models without internal reasoning mechanisms (e.g., Qwen2.5-7B-Instruct, Mistral-7B) might be more amenable to SFT with our current training data format.

---

## 9. Experimental Summary Table

| Experiment | Model | Dataset | Train/Test | Baseline | Fine-tuned | Delta | p-value |
|-----------|-------|---------|------------|----------|-----------|-------|---------|
| Mid-defence | Qwen3-14B | 288 (all types) | 230/58 | 8.6% | 13.8% | +5.2% | N/A |
| Llama 5-fold | Llama 3.1 8B | 256 (all types) | ~204/~51 | 37.5% | 39.8% | +2.4% | 0.25 |
| Qwen3 run 1 | Qwen3-8B | 215 (numeric) | 172/43 | 67.9% | 67.0% | -0.9% | 0.875 |
| Qwen3 run 2a | Qwen3-8B | 215 (numeric) | 172/43 | TBD | TBD | TBD | TBD |
| Qwen3 run 2b | Qwen3-8B | 215 (numeric) | 172/43 | TBD | TBD | TBD | TBD |
| Qwen3 run 2c | Qwen3-8B | 215 (numeric) | 172/43 | TBD | TBD | TBD | TBD |
| Qwen3 run 2d | Qwen3-8B | 215 (numeric) | 172/43 | TBD | TBD | TBD | TBD |

---

## 10. References

1. Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A., Khashabi, D., & Hajishirzi, H. (2023). Self-Instruct: Aligning Language Models with Self-Generated Instructions. *ACL 2023*. arXiv:2212.10560.
2. Zhang, Z., Zhang, A., Li, M., & Smola, A. (2022). Automatic Chain of Thought Prompting in Large Language Models. arXiv:2210.03493.
3. Ding, B. et al. (2024). Data Augmentation using Large Language Models: Data Perspectives, Learning Paradigms and Challenges. arXiv:2403.02990.
4. Ranaldi, L. & Freitas, A. (2024). Self-Refine Instruction-Tuning for Aligning Reasoning in Language Models. *EMNLP 2024*.
5. Jain, N. et al. (2023). NEFTune: Noisy Embeddings Improve Instruction Finetuning. arXiv:2310.05914.
6. Xu, C. et al. (2023). WizardLM: Empowering Large Language Models to Follow Complex Instructions. arXiv:2304.12244.
7. Taori, R. et al. (2023). Stanford Alpaca: An Instruction-Following LLaMA Model. Stanford CRFM.
8. Shumailov, I. et al. (2024). The Curse of Recursion: Training on Generated Data Makes Models Forget. *Nature*.
9. Yu, H. et al. (2024). CoT-Self-Instruct. arXiv:2405.00402.
10. Li, X. et al. (2025). SearchInstruct: Domain-Specific Instruction Data Generation via RAG. arXiv:2509.10708.

---

## Appendix A: Repository Structure

```
Reliability-Domain-Specific-LLM/
├── data/
│   ├── master_dataset_cleaned.jsonl    # 256 items, final training data
│   ├── seed_dataset.json               # Original textbook extractions
│   ├── cross_model_verified.jsonl      # Verification results
│   ├── cv_splits/                      # 5-fold train/test splits
│   └── archive/                        # Earlier dataset iterations
├── training/
│   ├── config.py                       # Experiment config (env var overrides)
│   ├── train_sft.py                    # LoRA SFT training
│   ├── evaluate_baseline.py            # Base model evaluation
│   ├── evaluate_finetuned.py           # Fine-tuned model evaluation
│   ├── aggregate_results.py            # Cross-validation aggregation
│   ├── prepare_data.py                 # CV split generation
│   └── experiments/                    # Per-experiment SLURM scripts
├── generators/
│   ├── synthetic_data_generation.ipynb # Self-instruct generation
│   ├── cross_model_generation.ipynb    # Cross-model verification
│   └── reasoning_processor.py          # Reasoning chain validation
├── evaluators/
│   ├── baseline_small_models.ipynb     # Multi-model baseline eval
│   └── model_evaluation.ipynb          # General evaluation
├── extractors/
│   ├── textbook_qa_extractor.ipynb     # OCR -> Q/R/A extraction
│   ├── dataset_cleaning.ipynb          # Final cleaning pipeline
│   └── fix_unicode_latex_llm.ipynb     # LaTeX/Unicode fixing
├── results/
│   ├── sft_cv_llama3.1-8b/            # Llama results
│   ├── sft_cv_qwen3-8b/               # Qwen3 run 1 results
│   └── sft_cv_qwen3-8b-{v2,...}/      # Qwen3 run 2 results (pending)
├── literature/                         # Reference papers
├── ocr_output/                         # Textbook OCR markdown
└── utils/
    ├── api_client.py                   # OpenRouter API client
    └── data_io.py                      # JSONL I/O helpers
```

## Appendix B: Training Data Statistics

| Metric | Value |
|--------|-------|
| Total examples | 256 |
| Numeric answers | 215 (84%) |
| Formula answers | 21 (8%) |
| Text answers | 19 (7%) |
| Boolean answers | 1 (<1%) |
| Source: seed (textbook) | 98 (38%) |
| Source: cross_model_verified (synthetic) | 158 (62%) |
| Unique problem contexts | ~140 (69% are multi-part clusters) |
| Mean reasoning length | 69 words |
| Reasoning < 50 words | 36% |
| Answer-reasoning rounding mismatches | 24% |
