"""
prompt_manager.py
Utility to load and access prompt templates dynamically.
"""

import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompt_templates")

def load_prompt(prompt_name):
    """
    Load a prompt template by filename (without .py extension).
    Returns the raw string content of the prompt.
    """
    filename = f"{prompt_name}.py"
    file_path = os.path.join(PROMPT_DIR, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt '{prompt_name}' not found at {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Extract content between triple quotes (""")
    prompt_lines = []
    inside_quotes = False
    for line in lines:
        if '"""' in line:
            inside_quotes = not inside_quotes
            continue
        if inside_quotes:
            prompt_lines.append(line.rstrip())

    return "\n".join(prompt_lines)


# Example usage
if __name__ == "__main__":
    try:
        prompt_text = load_prompt("intro_prompt")
        print("Loaded Prompt:")
        print(prompt_text)
    except Exception as e:
        print(f"Error: {e}")
