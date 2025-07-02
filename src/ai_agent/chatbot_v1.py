"""
chatbot_v1.py
Basic chatbot loop using language detection and prompt context loading.
"""

from contextual_prompt_loader import detect_language, load_prompt

def chatbot_loop():
    print("👋 Welcome to WealthReportBDAI Chatbot (v1)")
    print("Type 'exit' to end the conversation.")

    session_context = {
        "started": False,
        "language": "en"
    }

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you. Goodbye! 👋")
            break

        # Detect language only on first message
        if not session_context["started"]:
            lang = detect_language(user_input)
            session_context["language"] = lang
            session_context["started"] = True
            prompt = load_prompt(lang, "intro")
        else:
            # After intro, move to followup or will based on keyword
            if "will" in user_input.lower() or "উইল" in user_input:
                prompt = load_prompt(session_context["language"], "will")
            else:
                prompt = load_prompt(session_context["language"], "followup")

        print(f"Bot:\n{prompt}")

if __name__ == "__main__":
    chatbot_loop()
