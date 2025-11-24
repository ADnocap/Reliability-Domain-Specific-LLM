# Domain-Specific LLM for Reliability Engineering

**Research Project** | CentraleSupélec - LGI Laboratory  
**Supervisor**: Zhiguo Zeng
**Group Members**: Alex Dalban, Elora

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

## References

1. **Self-Instruct**: Wang, Y. et al. Self-Instruct: Aligning Language Models with Self-Generated Instructions. [arXiv:2212.10560](https://doi.org/10.48550/arXiv.2212.10560) (2023)

2. **Chain-of-Thought**: Zhang, Z., Zhang, A., Li, M. & Smola, A. Automatic Chain of Thought Prompting in Large Language Models. [arXiv:2210.03493](https://doi.org/10.48550/arXiv.2210.03493) (2022)

3. **Data Augmentation**: Ding, B. et al. Data Augmentation using Large Language Models: Data Perspectives, Learning Paradigms and Challenges. [arXiv:2403.02990](https://doi.org/10.48550/arXiv.2403.02990) (2024)

4. **Self-Refine**: Ranaldi, L. & Freitas, A. Self-Refine Instruction-Tuning for Aligning Reasoning in Language Models. Proceedings of EMNLP 2024. [doi:10.18653/v1/2024.emnlp-main.139](https://doi.org/10.18653/v1/2024.emnlp-main.139)

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
