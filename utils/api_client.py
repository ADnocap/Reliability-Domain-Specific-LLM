"""OpenRouter API client factory."""

import os
from openai import OpenAI
from dotenv import load_dotenv


def create_openrouter_client(api_key=None) -> OpenAI:
    """Create an OpenAI client configured for OpenRouter.

    Args:
        api_key: OpenRouter API key. If not provided, loads from
                 the OPENROUTER_API_KEY environment variable (or .env file).

    Returns:
        An OpenAI client pointing at the OpenRouter API.
    """
    if api_key is None:
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY", "")

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
