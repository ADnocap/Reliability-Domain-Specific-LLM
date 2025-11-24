import re


def clean_text(text):
    """Remove citations and clean whitespace"""
    text = re.sub(r'\[[\d,\s.p]+\]', '', text)
    text = re.sub(r'\([A-Z][a-z]+(?:\s+(?:and|et al\.?)\s+[A-Z][a-z]+)*\s+\d{4}(?:;\s*[A-Z][a-z]+(?:\s+(?:and|et al\.?)\s+[A-Z][a-z]+)*\s+\d{4})*\)', '', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()


def find_solution_position(text):
    """Find where 'Solution' keyword starts in text"""
    pattern = r'\bsolution\s*[\d.]*:?'
    match = re.search(pattern, text, re.IGNORECASE)
    return match.start() if match else None


def extract_boxed_content(text):
    """Extract content from \boxed{...} LaTeX notation with balanced braces"""
    match = re.search(r'\\boxed\{', text)
    if not match:
        return None
    
    start = match.end()
    brace_count = 1
    i = start
    
    while i < len(text) and brace_count > 0:
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
            continue
        if text[i] == '{':
            brace_count += 1
        elif text[i] == '}':
            brace_count -= 1
        i += 1
    
    return text[start:i-1] if brace_count == 0 else None


def normalize_answer(answer):
    """Normalize answer for comparison"""
    answer = answer.lower().strip()
    answer = answer.rstrip('.,;:!?')
    answer = ' '.join(answer.split())
    return answer
