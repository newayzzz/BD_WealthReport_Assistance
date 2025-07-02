"""
prompt_dict_loader.py
Loads all .txt-based prompts from the prompt_templates_txt folder into a dictionary.
"""

import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompt_templates_txt")

def load_all_prompts():
    prompts = {}
    for filename in os.listdir(PROMPT_DIR):
        if filename.endswith(".txt"):
            prompt_name = filename.replace(".txt", "")
            file_path = os.path.join(PROMPT_DIR, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                prompts[prompt_name] = f.read().strip()
    return prompts

# Example usage
if __name__ == "__main__":
    prompts = load_all_prompts()
    for name, content in prompts.items():
        print(f"--- {name} ---\n{content}\n")
