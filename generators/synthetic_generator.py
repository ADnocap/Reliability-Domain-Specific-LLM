import json
import random
import re
import os
import time
from typing import List, Dict, Optional, Tuple
from utils.text_processing import extract_boxed_content
from utils.api_client import APIClient


class SyntheticGenerator:
    """Generate synthetic questions with consistency checking"""
    
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
    
    def load_seeds(self, filepath: str) -> List[str]:
        """Load seed questions from JSONL"""
        questions = []
        with open(filepath, 'r') as f:
            for line in f:
                data = json.loads(line)
                questions.append(data['question'])
        return questions
    
    def parse_response(self, response: str) -> Optional[Dict[str, str]]:
        """Parse generated question and answer from response"""
        try:
            q_match = re.search(
                r'\[New Question Begin\](.*?)\[New Question End\]',
                response,
                re.DOTALL | re.IGNORECASE
            )
            question = q_match.group(1).strip() if q_match else None
            
            answer = None
            a_match = re.search(
                r'\[Final Answer to New Question Begin\](.*?)\[Final Answer to New Question End\]',
                response,
                re.DOTALL | re.IGNORECASE
            )
            
            if a_match:
                answer_section = a_match.group(1)
                answer = extract_boxed_content(answer_section)
                if answer is None:
                    answer = answer_section.strip()
            
            if not question or not answer:
                return None
            
            return {"question": question, "answer": answer}
        
        except Exception:
            return None
    
    def generate_question(self, seed_questions: List[str], model: str,
                         num_seeds: int = 2) -> Optional[Dict[str, str]]:
        """Generate a new question based on seeds"""
        sampled = random.sample(seed_questions, min(num_seeds, len(seed_questions)))
        
        prompt = """You are a reasoning question generator. Create a novel, challenging reasoning question.

Seed questions:
"""
        for i, q in enumerate(sampled, 1):
            prompt += f"{i}. {q}\n"
        
        prompt += """
Your task:
1. Write a brand-new question that:
   - Draws inspiration from seeds without copying
   - Is mathematical or logical with a definite answer
   - Is NOT multi-part; focus on a single problem
   - Answer must be ONE of these formats:
     * A single number: 42, 3.14, 0.1353
     * A simple fraction: 1/2, 3/4
     * A simple expression with ONE variable: 2x, x^2
     * A boolean: True or False
     * A single choice: A, B, C, or D

2. Reason step by step to solve it

3. Express final answer in SIMPLEST NUMERICAL FORM:
   - Decimals: round to 4 places
   - Fractions: reduce completely
   - No units or text in the answer
   - No variable assignments unless answer requires it

Format your response EXACTLY as:
[New Question Begin]
your question here
[New Question End]

[Step-by-step Solution Begin]
your solution here
[Step-by-step Solution End]

[Final Answer to New Question Begin]
\\boxed{your answer}
[Final Answer to New Question End]"""
        
        response = self.api_client.call(
            prompt=prompt,
            model=model,
            temperature=0.5,
            max_tokens=2000
        )
        
        if not response:
            return None
        
        return self.parse_response(response)
    
    def check_consistency(self, question: str, expected_answer: str, model: str,
                         num_samples: int = 3, threshold: float = 0.5) -> Tuple[bool, float]:
        """Check answer consistency across multiple samples"""
        prompt = f"""Solve this problem and give ONLY the final answer:

{question}

Respond with ONLY the final numerical answer (no explanation)."""
        
        answers = []
        for _ in range(num_samples):
            response = self.api_client.call(
                prompt=prompt,
                model=model,
                temperature=0.6,
                max_tokens=200
            )
            if response:
                answers.append(response.lower().strip())
        
        if not answers:
            return False, 0.0
        
        expected_norm = expected_answer.lower().strip()
        matches = sum(1 for a in answers if expected_norm in a or a in expected_norm)
        score = matches / len(answers)
        
        return score >= threshold, score
    
    def generate_dataset(self, seed_file: str, output_file: str, num_attempts: int,
                        model: str, consistency_threshold: float = 0.5,
                        num_consistency_samples: int = 3) -> List[Dict]:
        """Generate and filter synthetic questions"""
        seed_questions = self.load_seeds(seed_file)
        dataset = []
        
        for i in range(num_attempts):
            print(f"\nGenerating question {i+1}/{num_attempts}...")
            
            tokens_before = self.api_client.get_token_count()
            
            synthetic = self.generate_question(seed_questions, model)
            
            if synthetic is None:
                print("  Failed to parse")
                continue
            
            passes, score = self.check_consistency(
                synthetic['question'],
                synthetic['answer'],
                model,
                num_samples=num_consistency_samples,
                threshold=consistency_threshold
            )
            
            tokens_used = self.api_client.get_token_count() - tokens_before
            
            if passes:
                synthetic['consistency_score'] = score
                synthetic['tokens_used'] = tokens_used
                dataset.append(synthetic)
                
                with open(output_file, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(synthetic, ensure_ascii=False) + '\n')
                
                print(f"  ✓ Accepted (score={score:.2f}, tokens={tokens_used:,})")
            else:
                print(f"  ✗ Rejected (score={score:.2f}, tokens={tokens_used:,})")
            
            if i % 5 == 0:
                print(f"  Tokens used so far: {self.api_client.get_token_count():,}")
        
        print(f"\n{'='*60}")
        print(f"Generated {len(dataset)}/{num_attempts} quality questions")
        print(f"Total tokens: {self.api_client.get_token_count():,}")
        print(f"{'='*60}")
        
        return dataset
