"""
chatbot_ai.py
Chatbot that uses OpenAI GPT to respond instead of static prompt templates.
"""

import openai
import os

# Load API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_response(messages):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def chatbot_loop():
    print("🤖 GPT-powered WealthReportBDAI Chatbot")
    print("Type 'exit' to end the conversation.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant who helps Bengali families organize their financial assets such as LIC, PF, gold, FDs, SIPs, land, etc., and guides them with reminders and digital will instructions."}
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
