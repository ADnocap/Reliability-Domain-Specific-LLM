# Domain-Specific LLM for Reliability Engineering

**Research Project** | CentraleSupélec - LGI Laboratory  
**Supervisor**: Zhiguo Zeng
**Group Members**: Alex Dalban, Elora Drouilhet

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

## Repository Structure

```
├── utils/                  # Shared Python modules
│   ├── api_client.py       #   OpenRouter client factory
│   └── data_io.py          #   JSON/JSONL load/save helpers
├── data/                   # Datasets
│   ├── seed_dataset.json   #   Primary cleaned dataset (56 items)
│   ├── seed_extended.jsonl #   Extended JSONL version (66 items)
│   ├── seed_latex_cleaned.jsonl  # After LaTeX/unicode fix (63 items)
│   ├── seed_subset_49.jsonl      # Filtered subset (49 items)
│   └── archive/            #   Earlier extraction iterations
├── extractors/             # Data extraction from textbooks
│   ├── textbook_qa_extractor.ipynb
│   └── fix_unicode_latex_llm.ipynb
├── generators/             # Synthetic data generation
│   ├── synthetic_data_generation.ipynb
│   ├── jsonl_to_markdown.py
│   └── reasoning_processor.py
├── evaluators/             # Model evaluation
│   └── model_evaluation.ipynb
├── results/                # Evaluation results
├── literature/             # Reference papers
├── ocr_output/             # OCR-extracted textbook markdown
└── textbooks/              # Source textbook PDFs (git-ignored)
```
