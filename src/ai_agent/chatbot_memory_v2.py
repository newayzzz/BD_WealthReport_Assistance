"""
chatbot_v2.py
Chatbot with basic memory for storing user answers.
"""

from contextual_prompt_loader import detect_language, load_prompt

def chatbot_loop():
    print("👋 Welcome to WealthReportBDAI Chatbot (v2 with memory)")
    print("Type 'exit' to end the conversation.")

    session_context = {
        "started": False,
        "language": "en",
        "assets_collected": [],
        "digital_will_ready": False
    }

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you. Here's a summary of what you shared:")
            for idx, asset in enumerate(session_context["assets_collected"], 1):
                print(f"  {idx}. {asset}")
            print("👋 Goodbye!")
            break

        # Detect language only once
        if not session_context["started"]:
            lang = detect_language(user_input)
            session_context["language"] = lang
            session_context["started"] = True
            prompt = load_prompt(lang, "intro")
        else:
            # Check for will-related message
            if "will" in user_input.lower() or "উইল" in user_input:
                session_context["digital_will_ready"] = True
                prompt = load_prompt(session_context["language"], "will")
            else:
                # Store this message as an asset mention
                session_context["assets_collected"].append(user_input.strip())
                prompt = load_prompt(session_context["language"], "followup")

        print(f"Bot:\n{prompt}")

if __name__ == "__main__":
    chatbot_loop()
