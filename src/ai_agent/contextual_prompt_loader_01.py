"""
contextual_prompt_loader.py
Load appropriate prompts based on both language and interaction context.
"""

from langdetect import detect
import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompt_templates")

# Updated prompt map with full Bengali and English context support
PROMPT_MAP = {
    "en": {
        "intro": "intro_prompt.txt",
        "followup": "followup_asset_prompt.txt",
        "will": "digital_will_prompt.txt"
    },
    "bn": {
        "intro": "bengali_intro_prompt.txt",
        "followup": "bengali_followup_asset_prompt.txt",
        "will": "bengali_digital_will_prompt.txt"
    }
}

def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "en"  # Default fallback

def load_prompt(language_code, context_type, fallback_lang="en"):
    """
    Load prompt based on language and context type ('intro', 'followup', 'will')
    """
    lang_prompts = PROMPT_MAP.get(language_code, PROMPT_MAP[fallback_lang])
    filename = lang_prompts.get(context_type, PROMPT_MAP[fallback_lang].get(context_type))
    if not filename:
        raise ValueError(f"No prompt defined for context: {context_type}")
    path = os.path.join(PROMPT_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    context = input("Enter context (intro/followup/will): ").strip().lower()
    lang = detect_language(user_input)
    prompt = load_prompt(lang, context)
    print(f"\n[Language Detected: {lang}, Context: {context}]\nPrompt:\n{prompt}")
