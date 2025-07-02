"""
chatbot_v3_logging.py
Auto-switching chatbot with CSV logging of Q&A sessions.
"""

import csv
from datetime import datetime
from llm_router import generate_response

def chatbot_loop():
    print("🤖 Smart LLM-Routed WealthReportBDAI Chatbot (v3 + CSV Logging)")
    print("Type 'exit' to end the conversation.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant that helps Bengali families track financial assets like LIC, PF, gold, land, SIP, etc., and supports digital will creation."}
    ]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"wealth_chat_session_{timestamp}.csv"
    log_path = os.path.join("chat_logs", log_file)
    os.makedirs("chat_logs", exist_ok=True)

    with open(log_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["User", "Bot"])  # Header

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
                writer.writerow([user_input, reply])
            except Exception as e:
                print(f"❌ Error: {e}")
                break

if __name__ == "__main__":
    chatbot_loop()
