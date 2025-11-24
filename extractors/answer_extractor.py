import re
import json
from pathlib import Path
from typing import Optional, Dict, List
from utils.text_processing import clean_text, find_solution_position, extract_boxed_content
from utils.api_client import APIClient


class AnswerExtractor:
    """Extract concise final answers from textbook solutions"""
    
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
        self.question_keywords = ['example', 'problem', 'exercise', 'homework']
    
    def extract_solution_chunk(self, text: str, keyword: str, number: str,
                               chunk_size: int = 1000) -> Optional[str]:
        """Extract solution text after finding the question"""
        pattern = rf'\b{re.escape(keyword)}\s+{re.escape(number)}'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if not match:
            return None
        
        content = text[match.end():]
        solution_pos = find_solution_position(content)
        
        if solution_pos is None:
            return None
        
        solution_chunk = content[solution_pos:solution_pos + chunk_size]
        return clean_text(solution_chunk)
    
    def extract_answer_with_llm(self, question: str, solution_chunk: str) -> Optional[str]:
        """Use LLM to extract final answer from solution"""
        prompt = f"""You are an answer extraction assistant. Given a question and its solution text, extract ONLY the final answer.

Question:
{question}

Solution text:
{solution_chunk}

Your task:
1. Check if the solution text contains the final answer
2. If YES, extract ONLY the final answer in its SIMPLEST form:
   - A single number: e.g., 42, 3.14, 0.5
   - A simple fraction: e.g., 1/2, 3/4
   - A simple expression: e.g., 2x, x^2
   - A boolean: True or False
   - Multiple parts separated by commas: e.g., 0.3, 0.4, 0.5
3. If NO answer is found, respond with: NOT_FOUND

IMPORTANT:
- Extract ONLY the final answer, no explanation
- Do NOT include units or text descriptions
- Do NOT include "=" unless it's part of the answer format
- If the answer is in \\boxed{{...}}, extract just the content inside
- Return the answer in the simplest form possible

Respond with either the answer OR "NOT_FOUND"."""
        
        response = self.api_client.call(
            prompt=prompt,
            temperature=0.3,
            max_tokens=200
        )
        
        if not response or "NOT_FOUND" in response:
            return None
        
        boxed = extract_boxed_content(response)
        if boxed:
            return boxed
        
        return response.strip()
    
    def process_validated_questions(self, questions_jsonl: str, base_path: str,
                                    output_jsonl: str, chunk_size: int = 1000,
                                    verbose: bool = True) -> int:
        """Process validated questions and extract answers"""
        textbook_cache = {}
        successful = 0
        llm_failed = 0
        
        with open(questions_jsonl, 'r', encoding='utf-8') as qfile, \
             open(output_jsonl, 'w', encoding='utf-8') as outfile:
            
            questions = [json.loads(line) for line in qfile]
            
            for idx, q_data in enumerate(questions, 1):
                source = q_data['source']
                question = q_data['question']
                
                match = re.match(r'\[([^\]]+)\]\s+(\w+)\s+([\d.]+)', source)
                if not match:
                    continue
                
                filename, keyword, number = match.groups()
                file_path = f"{base_path}/{filename}.md"
                
                if filename not in textbook_cache:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            textbook_cache[filename] = f.read()
                        if verbose:
                            print(f"Loaded: {filename}.md")
                    except FileNotFoundError:
                        continue
                
                text = textbook_cache[filename]
                solution_chunk = self.extract_solution_chunk(text, keyword, number, chunk_size)
                
                if not solution_chunk:
                    continue
                
                answer = self.extract_answer_with_llm(question, solution_chunk)
                
                if answer:
                    outfile.write(json.dumps({
                        'source': source,
                        'question': question,
                        'answer': answer
                    }, ensure_ascii=False) + '\n')
                    successful += 1
                    if verbose:
                        print(f"Question {idx} ({source}): ✓ Answer extracted")
                else:
                    llm_failed += 1
                    if verbose:
                        print(f"Question {idx} ({source}): LLM could not extract answer")
                
                if verbose and idx % 10 == 0:
                    print(f"  Progress: {idx}/{len(questions)} processed, {successful} successful, {self.api_client.get_token_count():,} tokens\n")
        
        print(f"\n{'='*60}")
        print("Answer extraction complete:")
        print(f"  Successful pairs:   {successful}")
        print(f"  LLM could not find: {llm_failed}")
        print(f"  Total processed:    {len(questions)}")
        print(f"  Success rate:       {successful / len(questions) * 100:.1f}%")
        print(f"  Total tokens used:  {self.api_client.get_token_count():,}")
        print(f"{'='*60}")
        print(f"Output saved to: {output_jsonl}")
        
        return successful
