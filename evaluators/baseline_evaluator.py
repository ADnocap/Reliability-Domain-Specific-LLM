import json
import time
from typing import Dict, List, Optional
from utils.text_processing import normalize_answer
from utils.api_client import APIClient


class BaselineEvaluator:
    """Evaluate baseline model performance on Q&A datasets"""
    
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
    
    def check_equivalence(self, answer1: str, answer2: str, question: str = "") -> bool:
        """Use LLM to check semantic equivalence"""
        context = f"Question: {question}\n\n" if question else ""
        
        prompt = f"""You are an answer equivalence checker.

{context}Model Answer: {answer1}

Ground Truth: {answer2}

The Model Answer is CORRECT if:
- It contains the ground truth answer
- It is mathematically/semantically equivalent
- Different notations that mean the same (0.5 = 1/2)
- Different formatting
- Minor rounding differences

The Model Answer is INCORRECT if:
- Different numerical value (beyond rounding)
- Contradictory answer
- Missing required parts
- Fundamentally misunderstands the question

Respond with ONLY "CORRECT" or "INCORRECT"."""
        
        response = self.api_client.call(
            prompt=prompt,
            model="mistralai/mistral-small-3.1-24b-instruct",
            temperature=0.1,
            max_tokens=50
        )
        
        return response and "CORRECT" in response.upper() and "INCORRECT" not in response.upper()
    
    def evaluate_single(self, question: str, ground_truth: str, model: str) -> Dict:
        """Evaluate a single question-answer pair"""
        prompt = f"""Solve this problem and provide ONLY the final answer:

{question}

Provide ONLY the numerical answer (no explanation)."""
        
        model_answer = self.api_client.call(
            prompt=prompt,
            model=model,
            temperature=0.3,
            max_tokens=1000,
            max_retries=10
        )
        
        if not model_answer:
            return {
                'model_answer': None,
                'correct': False,
                'comparison_method': 'api_failure'
            }
        
        norm_model = normalize_answer(model_answer)
        norm_truth = normalize_answer(ground_truth)
        
        if norm_model == norm_truth:
            return {
                'model_answer': model_answer,
                'correct': True,
                'comparison_method': 'direct_match'
            }
        
        is_correct = self.check_equivalence(model_answer, ground_truth, question)
        
        return {
            'model_answer': model_answer,
            'correct': is_correct,
            'comparison_method': 'llm_equivalence'
        }
    
    def evaluate_dataset(self, input_jsonl: str, output_jsonl: str, stats_jsonl: str,
                        models: List[str], max_questions: Optional[int] = None,
                        verbose: bool = True) -> Dict:
        """Evaluate multiple models on dataset"""
        with open(input_jsonl, 'r', encoding='utf-8') as f:
            questions = [json.loads(line) for line in f]
        
        if max_questions:
            questions = questions[:max_questions]
        
        model_names = {m: m.split('/')[-1] for m in models}
        
        stats = {
            m: {'correct': 0, 'incorrect': 0, 'api_failures': 0,
                'direct_matches': 0, 'llm_matches': 0}
            for m in models
        }
        
        with open(output_jsonl, 'w', encoding='utf-8') as outfile:
            for q_idx, q_data in enumerate(questions, 1):
                question = q_data['question']
                answer = q_data['answer']
                source = q_data.get('source', 'unknown')
                
                if verbose:
                    print(f"\nQuestion {q_idx}/{len(questions)} ({source}):")
                
                result = {
                    'question': question,
                    'answer': answer,
                    'source': source
                }
                
                for model in models:
                    model_short = model_names[model]
                    if verbose:
                        print(f"  Evaluating {model_short}...", end=" ")
                    
                    eval_result = self.evaluate_single(question, answer, model)
                    
                    if eval_result['model_answer'] is None:
                        stats[model]['api_failures'] += 1
                    elif eval_result['correct']:
                        stats[model]['correct'] += 1
                        if eval_result['comparison_method'] == 'direct_match':
                            stats[model]['direct_matches'] += 1
                        else:
                            stats[model]['llm_matches'] += 1
                    else:
                        stats[model]['incorrect'] += 1
                    
                    result[f'answer_{model_short}'] = eval_result['model_answer'] or "[API_FAILURE]"
                    result[f'is_correct_{model_short}'] = eval_result['correct']
                    
                    if verbose:
                        status = "✓" if eval_result['correct'] else "✗"
                        print(f"{status} {eval_result['comparison_method']}")
                
                outfile.write(json.dumps(result, ensure_ascii=False) + '\n')
                
                if verbose and q_idx % 5 == 0:
                    print(f"\n  Progress: {q_idx}/{len(questions)}, {self.api_client.get_token_count():,} tokens\n")
        
        summary = {}
        for model in models:
            total = stats[model]['correct'] + stats[model]['incorrect']
            accuracy = stats[model]['correct'] / total if total > 0 else 0
            
            summary[model] = {
                'model_name': model,
                'short_name': model_names[model],
                'correct': stats[model]['correct'],
                'incorrect': stats[model]['incorrect'],
                'api_failures': stats[model]['api_failures'],
                'direct_matches': stats[model]['direct_matches'],
                'llm_matches': stats[model]['llm_matches'],
                'total': total,
                'accuracy': accuracy
            }
        
        with open(stats_jsonl, 'w', encoding='utf-8') as f:
            json.dump({
                'total_questions': len(questions),
                'total_tokens_used': self.api_client.get_token_count(),
                'model_stats': summary
            }, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*80}")
        print("Evaluation Summary:")
        print(f"{'='*80}")
        
        for model in models:
            s = summary[model]
            print(f"\nModel: {model}")
            print(f"  Accuracy:      {s['accuracy']*100:.2f}% ({s['correct']}/{s['total']})")
            print(f"  Direct match:  {s['direct_matches']}")
            print(f"  LLM match:     {s['llm_matches']}")
            print(f"  Incorrect:     {s['incorrect']}")
            print(f"  API failures:  {s['api_failures']}")
        
        print(f"\nTotal tokens: {self.api_client.get_token_count():,}")
        print(f"{'='*80}")
        print(f"Results: {output_jsonl}")
        print(f"Stats: {stats_jsonl}")
        
        return summary
