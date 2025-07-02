"""
chatbot_fetch_ai.py
Chatbot using Fetch API with ASI1 mini LLM (hypothetical Fetch AI interface).
"""

import requests
import os

FETCH_API_KEY = os.getenv("FETCH_API_KEY")
FETCH_API_URL = "https://api.fetch.ai/v1/chat/completions"

def generate_response(messages):
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

def chatbot_loop():
    print("🤖 Fetch AI (ASI1 Mini) - WealthReportBDAI Chatbot")
    print("Type 'exit' to end the conversation.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant that helps Bengali families organize their assets such as LIC, PF, land, gold, etc., and supports digital will creation."}
    ]

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you for using WealthReportBDAI. Goodbye! 👋")
            break

        messages.append({"role": "user", "content": user_input})
        try:
            reply = generate_response(messages)
            messages.append({"role": "assistant", "content": reply})
            print(f"Bot:\n{reply}")
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    chatbot_loop()
