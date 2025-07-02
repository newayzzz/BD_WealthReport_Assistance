"""
chatbot_v3.py
Chatbot that uses llm_router.py to auto-switch between Fetch AI and OpenAI.
"""

from llm_router import generate_response

def chatbot_loop():
    print("🤖 Smart LLM-Routed WealthReportBDAI Chatbot (v3)")
    print("Type 'exit' to end the conversation.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant that helps Bengali families track financial assets like LIC, PF, gold, land, SIP, etc., and supports digital will creation."}
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
            print(f"❌ Error: {e}")
            break

if __name__ == "__main__":
    chatbot_loop()
