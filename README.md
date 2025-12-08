# Domain-Specific LLM for Reliability Engineering

**Research Project** | CentraleSupélec - LGI Laboratory  
**Supervisor**: Zhiguo Zeng
**Group Members**: Alex Dalban, Elora D

Fine-tuning Large Language Models for reliability engineering through self-instruct synthetic data generation.

---

## Project Overview

### Context

Engineers working with complex systems (nuclear plants, aircraft, electrical grids) require sophisticated reliability, risk, and safety analysis tools. Currently, reliability engineering requires significant manual programming effort by experienced engineers.

While general-purpose LLMs (like GitHub Copilot) excel at standard programming tasks, they consistently fail at reliability-specific coding problems. Previous work with ~50 hand-written reliability coding tasks showed that state-of-the-art LLMs:

- Provide incorrect or nonsensical code
- Fail to grasp reliability engineering concepts
- Cannot reason through multi-step domain problems

**Root cause**: Lack of specialized reliability engineering knowledge in general pre-training data.

### Goals

This project develops a domain-specific LLM for reliability engineering by:

1. **Synthetic Data Generation**: Automatically generate large-scale question-answer pairs from reliability textbooks using self-instruct fine-tuning
2. **Chain-of-Thought Integration**: Generate step-by-step reasoning processes for complex reliability problems
3. **Model Fine-Tuning**: Fine-tune pre-trained LLMs on synthetic data and evaluate against baseline

### Expected Deliverables

- Fine-tuned LLM for reliability engineering domain
- Large-scale synthetic Q&A dataset
- Comprehensive evaluation against baseline
- Research paper (if results warrant publication)
- Complete codebase and documentation

---

## What This Repository Does

This codebase implements the **data pipeline** for creating high-quality training data from reliability engineering textbooks. It extracts, validates, and generates question-answer pairs that will be used to fine-tune domain-specific LLMs.

### Pipeline Architecture

```
Reliability Textbooks (Markdown/PDF)
         ↓
   [1] Extract Questions
         ↓ (Regex + Structure)
   [2] Validate with LLM
         ↓ (Filter incomplete/invalid)
   [3] Extract Answers
         ↓ (LLM + Solution parsing)
   [4] Generate Synthetic Q&A
         ↓ (Self-instruct + CoT)
   [5] Evaluate Baseline Models
         ↓
Training Dataset for Fine-Tuning
```

---

## Usage

### 1. Data Generation Pipeline

Open `pipeline.ipynb` and run sections sequentially:

#### Section 1: Extract Questions

Extracts questions from textbook markdown files using keyword patterns (`Example`, `Problem`, `Exercise`, `Homework`).

```python
from extractors.question_extractor import QuestionExtractor

extractor = QuestionExtractor()
questions = extractor.process_multiple_files(file_paths, 'all_questions.jsonl')
```

**Output**: `content/all_questions.jsonl` (~hundreds of questions)

#### Section 2: Validate Questions

Uses LLM to filter out invalid questions (incomplete, referencing missing figures, etc.).

```python
from utils.api_client import APIClient

api_client = APIClient(api_key)
extractor = QuestionExtractor(api_client)
valid_count = extractor.validate_questions('all_questions.jsonl', 'valid_questions.jsonl')
```

**Output**: `content/validated_textbook2.jsonl` (filtered subset)

#### Section 3: Extract Answers

Finds solution sections in textbooks and uses LLM to extract concise final answers.

```python
from extractors.answer_extractor import AnswerExtractor

answer_extractor = AnswerExtractor(api_client)
pairs = answer_extractor.process_validated_questions(
    questions_jsonl='valid_questions.jsonl',
    base_path='./mistral ocr',
    output_jsonl='question_answer_pairs.jsonl'
)
```

**Output**: `content/question_answer_pairs.jsonl` (Q&A pairs ready for training)

#### Section 4: Generate Synthetic Data

Uses self-instruct to generate new questions inspired by seed questions, with consistency checking.

```python
from generators.synthetic_generator import SyntheticGenerator

generator = SyntheticGenerator(api_client)
dataset = generator.generate_dataset(
    seed_file='valid_questions.jsonl',
    output_file='synthetic_questions.jsonl',
    num_attempts=100,
    consistency_threshold=0.5
)
```

**Output**: `content/synthetic_questions.jsonl` (synthetic Q&A pairs)

### 2. Baseline Evaluation

Open `evaluation.ipynb` to evaluate model performance:

```python
from evaluators.baseline_evaluator import BaselineEvaluator

evaluator = BaselineEvaluator(api_client)

summary = evaluator.evaluate_dataset(
    input_jsonl='question_answer_pairs.jsonl',
    output_jsonl='baseline_results.jsonl',
    stats_jsonl='baseline_stats.json',
    models=['openai/gpt-4o-mini', 'deepseek/deepseek-r1-distill-qwen-14b']
)
```

**Evaluation Metrics**:

- Accuracy (correct answers vs total)
- Direct string matching rate
- LLM semantic equivalence rate
- Token usage statistics

**Output**:

- `baseline results/baseline_results_*.jsonl` - Detailed results
- `baseline results/baseline_stats_*.json` - Summary statistics

---

## Data Format

### Question Format (JSONL)

```json
{
  "source": "[file_14] Example 6.4.",
  "question": "Calculate the reliability of a system with..."
}
```

### Question-Answer Format (JSONL)

```json
{
  "source": "[file_14] Example 6.4.",
  "question": "Calculate the reliability of a system with...",
  "answer": "0.8647"
}
```

### Synthetic Question Format (JSONL)

```json
{
  "question": "Determine the mean time to failure for...",
  "answer": "245.7",
  "consistency_score": 0.83,
  "tokens_used": 1250
}
```

### Evaluation Results Format (JSONL)

```json
{
  "question": "...",
  "answer": "0.8647",
  "source": "[file_14] Example 6.4.",
  "answer_gpt-4o-mini": "0.865",
  "is_correct_gpt-4o-mini": true,
  "answer_deepseek-r1": "0.8647",
  "is_correct_deepseek-r1": true
}
```

---

## Key Features

### Self-Instruct Fine-Tuning

- Automatically generates diverse Q&A pairs from textbook content
- Uses powerful LLMs as data generators
- Validates quality through consistency checking

### Chain-of-Thought (CoT) Integration

- Generates step-by-step reasoning for complex problems
- Teaches models _how to reason_, not just _what to answer_
- Critical for multi-step reliability engineering problems

### Robust Validation

- LLM-based question validation
- Answer consistency checking across multiple samples
- Semantic equivalence checking in evaluation

### Comprehensive Evaluation

- Direct string matching
- LLM-based semantic equivalence
- Token usage tracking
- Detailed per-question results

---

## Methodology

### Question Extraction

1. Parse textbook markdown files
2. Find questions using keyword patterns
3. Extract text until solution marker
4. Clean citations and formatting
5. Filter by length (50-1800 characters)

### LLM Validation

Questions must be:

- Self-contained and deterministic
- Answerable with provided information
- Require mathematical/technical reasoning
- Not reference missing figures/tables

### Answer Extraction

1. Locate question in textbook
2. Find solution section
3. Extract solution chunk (1000 chars)
4. Use LLM to identify final answer
5. Parse LaTeX `\boxed{...}` notation

### Synthetic Generation

1. Sample 2+ seed questions
2. Prompt LLM to generate inspired question
3. Generate step-by-step solution with CoT
4. Extract final answer
5. Verify consistency across 3+ samples
6. Accept if consistency score > 0.5

### Evaluation

1. Present question to model
2. Compare model answer to ground truth
3. Try direct string matching first
4. Use LLM semantic equivalence if no match
5. Track accuracy, method, and tokens

---

## Results

### Current Performance (Baseline)

**Seed Questions** (~288 Q&A pairs):

- GPT-5-mini: ~XX% accuracy
- DeepSeek-R1: ~XX% accuracy

**Synthetic Questions** (~50 generated):

- Consistency threshold: 0.5
- Average tokens per question: ~5,000
- Generation success rate: ~XX%

_See `baseline results/` for detailed statistics_

---

## Technical Implementation

### API Integration

- OpenRouter API for model access
- Automatic retry logic with exponential backoff
- Token usage tracking
- Rate limiting and timeout handling

### Text Processing

- Regex-based question detection
- LaTeX notation parsing (`\boxed{}`)
- Citation removal
- Answer normalization

### Quality Control

- Multi-sample consistency checking
- Semantic equivalence validation
- Length filtering
- Solution presence verification

---

## References

1. **Self-Instruct**: Wang, Y. et al. Self-Instruct: Aligning Language Models with Self-Generated Instructions. [arXiv:2212.10560](https://doi.org/10.48550/arXiv.2212.10560) (2023)

2. **Chain-of-Thought**: Zhang, Z., Zhang, A., Li, M. & Smola, A. Automatic Chain of Thought Prompting in Large Language Models. [arXiv:2210.03493](https://doi.org/10.48550/arXiv.2210.03493) (2022)

3. **Data Augmentation**: Ding, B. et al. Data Augmentation using Large Language Models: Data Perspectives, Learning Paradigms and Challenges. [arXiv:2403.02990](https://doi.org/10.48550/arXiv.2403.02990) (2024)

4. **Self-Refine**: Ranaldi, L. & Freitas, A. Self-Refine Instruction-Tuning for Aligning Reasoning in Language Models. Proceedings of EMNLP 2024. [doi:10.18653/v1/2024.emnlp-main.139](https://doi.org/10.18653/v1/2024.emnlp-main.139)

---

## Next Steps

### Phase 1: Data Pipeline (Current)

- ✅ Extract questions from textbooks
- ✅ Validate with LLM
- ✅ Extract answers from solutions
- ✅ Generate synthetic Q&A pairs
- ✅ Evaluate baseline models

### Phase 2: Model Fine-Tuning (Upcoming)

- [ ] Prepare training dataset (combine seed + synthetic)
- [ ] Select base model for fine-tuning
- [ ] Implement LoRA/QLoRA fine-tuning
- [ ] Train with Chain-of-Thought examples
- [ ] Validate on held-out test set

### Phase 3: Evaluation & Publication

- [ ] Compare fine-tuned vs baseline performance
- [ ] Analyze error patterns and failure modes
- [ ] Document methodology and results
- [ ] Prepare research paper
- [ ] Release fine-tuned model (if permissible)

---

## Configuration

### Environment Variables

Create a `.env` file:

```bash
OPENROUTER_API_KEY=sk-or-v1-...
```

### Key Parameters

**Question Extraction**:

- Keywords: `example`, `problem`, `exercise`, `homework`
- Length range: 50-1800 characters

**Answer Extraction**:

- Solution chunk size: 1000 characters
- Model: `mistralai/mistral-small-3.1-24b-instruct`

**Synthetic Generation**:

- Model: `qwen/qwen-2.5-72b-instruct`
- Consistency threshold: 0.5
- Consistency samples: 3-6
- Temperature: 0.5-0.6

**Evaluation**:

- Equivalence model: `mistralai/mistral-small-3.1-24b-instruct`
- Temperature: 0.3
- Max retries: 10

---

## Troubleshooting

### Common Issues

**"No images found in directory"**

- Check `BASE_PATH` points to correct textbook directory
- Verify markdown files exist (`file_1.md`, `file_2.md`, etc.)

**"API key not found"**

- Create `.env` file with `OPENROUTER_API_KEY`
- Load with `from dotenv import load_dotenv; load_dotenv()`

**"Empty API response"**

- Check API key is valid
- Verify network connectivity
- Increase `max_retries` parameter

**Low consistency scores in synthetic generation**

- Increase `num_consistency_samples`
- Adjust `consistency_threshold` (lower = more lenient)
- Try different models

---

## Contributing

This is an academic research project. For questions or collaboration:

**Contact**: Zhiguo Zeng - zhiguo.zeng@centralesupelec.fr  
**Institution**: LGI Laboratory, CentraleSupélec  
**Location**: 3 Rue Joliot-Curie, F-91192 Gif-sur-Yvette, France

---

## License

Academic research project - CentraleSupélec, 2024-2025

---

## Acknowledgments

- **Supervisor**: Zhiguo Zeng (LGI, CentraleSupélec)
- **Previous Work**: Prior student projects on LLM evaluation for reliability engineering
- **Resources**: Pre-processed textbook dataset, evaluation baseline (~50 questions)
- **Funding**: CentraleSupélec MSc AI program

---

## Citation

If you use this work in your research, please cite:

```bibtex
@misc{reliability-llm-2025,
  title={Domain-Specific LLM for Reliability Engineering through Self-Instruct Fine-Tuning},
  author={CentraleSupélec LGI Laboratory},
  year={2025},
  institution={CentraleSupélec},
  note={MSc AI Research Project}
}
```
