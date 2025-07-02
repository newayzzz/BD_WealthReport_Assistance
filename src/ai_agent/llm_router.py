"""
llm_router.py
Automatically routes requests to ASI1 (Fetch AI) or OpenAI based on tier.

Environment Variables:
- LLM_TIER = "free" or "premium"
- FETCH_API_KEY
- OPENAI_API_KEY
"""

import os
import requests
import openai

# Load config
LLM_TIER = os.getenv("LLM_TIER", "free").lower()
FETCH_API_KEY = os.getenv("FETCH_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

FETCH_API_URL = "https://api.fetch.ai/v1/chat/completions"
OPENAI_MODEL = "gpt-3.5-turbo"

def call_openai(messages):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0.5
    )
    return response.choices[0].message["content"]

def call_fetch_ai(messages):
    headers = {
        "Authorization": f"Bearer {FETCH_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "asi1-mini",
        "messages": messages,
        "temperature": 0.5
    }
    response = requests.post(FETCH_API_URL, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def generate_response(messages):
    if LLM_TIER == "premium":
        return call_openai(messages)
    else:
        return call_fetch_ai(messages)

# Example usage
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful financial assistant."},
        {"role": "user", "content": "আমার বাবার একটি LIC আছে।"}
    ]
    reply = generate_response(messages)
    print("Bot:", reply)
