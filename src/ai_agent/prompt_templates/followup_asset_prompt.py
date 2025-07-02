"""
Prompt: Ask for more asset details based on previous response
"""

FOLLOWUP_ASSET_PROMPT = """
Thank you. Let's go a bit deeper.

For each asset you mention (like LIC, FD, land, etc.), please tell me:
- The name of the person who owns it
- The name of the institution (e.g., LIC, Sonali Bank, etc.)
- Any key ID (policy number, account number if known)
- Approximate value, and when it matures or needs to be renewed
- Whether there's a nominee assigned

For example:
"My father's LIC at LIC of India is worth 5 lakhs, policy #123456, nominee is my mother. Next premium is in August."

You can list multiple assets at once too!
"""
