import re
import json
from pathlib import Path
from typing import List, Dict, Optional
from utils.text_processing import clean_text, find_solution_position
from utils.api_client import APIClient


class QuestionExtractor:
    """Extract and validate questions from textbook markdown files"""
    
    def __init__(self, api_client: Optional[APIClient] = None):
        self.question_keywords = ['example', 'problem', 'exercise', 'homework']
        self.api_client = api_client
    
    def find_questions(self, text: str, filename: Optional[str] = None) -> List[Dict]:
        """Find all questions in text"""
        questions = []
        keywords_pattern = '|'.join(self.question_keywords)
        pattern = rf'\b({keywords_pattern})\s+([\d.]+)'
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        
        for i, match in enumerate(matches):
            keyword = match.group(1)
            number = match.group(2)
            
            base_source = f"{keyword.title()} {number}"
            source = f"[{filename}] {base_source}" if filename else base_source
            
            question_start = match.end()
            while question_start < len(text) and text[question_start] in ' \t\n\r':
                question_start += 1
            
            if i < len(matches) - 1:
                content_end = matches[i + 1].start()
                has_next = True
            else:
                content_end = len(text)
                has_next = False
            
            content = text[question_start:content_end]
            solution_pos = find_solution_position(content)
            
            if has_next and solution_pos is None:
                continue
            
            if solution_pos is not None:
                question_text = content[:solution_pos].strip()
            else:
                question_text = content.strip()
            
            question_text = clean_text(question_text)
            
            if 50 < len(question_text) <= 1800:
                questions.append({
                    'source': source,
                    'question': question_text
                })
        
        return questions
    
    def process_file(self, input_file: str, filename: Optional[str] = None) -> List[Dict]:
        """Process a single markdown file"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"File not found: {input_file}")
            return []
        
        if filename is None:
            filename = input_file.split('/')[-1].replace('.md', '')
        
        return self.find_questions(text, filename=filename)
    
    def process_multiple_files(self, file_paths: List[str], output_file: str) -> List[Dict]:
        """Process multiple files and save to JSONL"""
        all_questions = []
        
        for file_path in file_paths:
            filename = file_path.split('/')[-1].replace('.md', '')
            questions = self.process_file(file_path, filename=filename)
            all_questions.extend(questions)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for q in all_questions:
                f.write(json.dumps(q, ensure_ascii=False) + '\n')
        
        print(f"Extracted {len(all_questions)} questions → {output_file}")
        return all_questions
    
    def validate_questions(self, input_jsonl: str, output_jsonl: str, 
                          verbose: bool = False) -> int:
        """Validate questions using LLM"""
        if self.api_client is None:
            raise ValueError("API client required for validation")
        
        validation_prompt = """You are validating textbook questions for a Q&A dataset.

A question is VALID if:
- It is self-contained with a clear, unambiguous answer
- It can be answered with the information provided
- It requires mathematical, technical, or conceptual reasoning
- It provides all necessary data and parameters

A question is NOT VALID if:
- It references figures, tables, or diagrams needed to answer it
- It says "use the above", "from the previous", etc. without providing that information
- It is too vague or open-ended
- It is a meta-question about the textbook itself
- The question text is cut off or incomplete

Respond with ONLY: "valid" or "not valid" (lowercase, no punctuation)."""
        
        valid_count = 0
        
        with open(input_jsonl, 'r', encoding='utf-8') as infile, \
             open(output_jsonl, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                data = json.loads(line)
                question_text = data['question']
                
                response = self.api_client.call(
                    prompt=f"{validation_prompt}\n\nQuestion to validate:\n\n{question_text}",
                    temperature=0.1
                )
                
                if response and "valid" in response.lower() and "not valid" not in response.lower():
                    outfile.write(line)
                    valid_count += 1
                    if verbose:
                        print(f"✓ {data['source']}")
        
        print(f"\nValidation complete: {valid_count} valid questions → {output_jsonl}")
        print(f"Tokens used: {self.api_client.get_token_count():,}")
        return valid_count
