"""
language_router.py
Detects the language of user input and selects the appropriate prompt file.
"""

from langdetect import detect
import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompt_templates")

def detect_language(text):
    """
    Detect the language of the input text.
    Returns 'bn' for Bengali, 'en' for English, etc.
    """
    try:
        return detect(text)
    except Exception as e:
        print(f"Language detection failed: {e}")
        return "en"  # Default fallback

def load_prompt(language_code, fallback="en"):
    """
    Load the appropriate prompt based on the language code.
    If not found, fallback to English.
    """
    lang_map = {
        "bn": "bengali_intro_prompt.txt",
        "en": "intro_prompt.txt"
    }
    filename = lang_map.get(language_code, lang_map[fallback])
    path = os.path.join(PROMPT_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Prompt not found for language: {language_code}. Using fallback.")
        return ""

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    lang = detect_language(user_input)
    prompt = load_prompt(lang)
    print(f"\n[Language Detected: {lang}]\nPrompt:\n{prompt}")
