import requests
import json
import time
from typing import Optional, Dict


class APIClient:
    """OpenRouter API client with retry logic and token tracking"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.total_tokens = 0
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
    
    def call(self, prompt: str, model: str = "mistralai/mistral-small-3.1-24b-instruct",
             temperature: float = 0.3, max_tokens: Optional[int] = None,
             max_retries: int = 3) -> Optional[str]:
        """
        Make API call with automatic retry on failure
        
        Args:
            prompt: Text prompt
            model: Model identifier
            temperature: Sampling temperature
            max_tokens: Maximum response tokens
            max_retries: Number of retry attempts
            
        Returns:
            Response text or None on failure
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        }
        
        if max_tokens:
            payload["max_tokens"] = max_tokens
        
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.base_url,
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                response.raise_for_status()
                
                if len(response.text.strip()) < 10:
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return None
                
                result = response.json()
                
                if 'choices' not in result or not result['choices']:
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return None
                
                content = result['choices'][0]['message']['content']
                
                if content is None or len(content.strip()) == 0:
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return None
                
                self.total_tokens += result.get('usage', {}).get('total_tokens', 0)
                return content.strip()
                
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    print(f"API Error: {e}")
                    return None
            except json.JSONDecodeError:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    return None
        
        return None
    
    def get_token_count(self) -> int:
        """Return total tokens used"""
        return self.total_tokens
    
    def reset_token_count(self):
        """Reset token counter"""
        self.total_tokens = 0
