# 💬 How to Use WealthReportBDAI Chatbot (Local Dev Guide)

This guide explains how to use the `llm_router.py` to automatically switch between **Fetch AI** (free tier) and **OpenAI** (premium tier) models within the WealthReportBDAI chatbot system.

---

## 🧠 LLM Auto-Switching

We use a smart router (`llm_router.py`) that dynamically picks the backend based on your environment:

| Tier     | Model Used       | API Key Required     |
|----------|------------------|----------------------|
| `free`   | ASI1-Mini (Fetch AI) | `FETCH_API_KEY` |
| `premium`| gpt-3.5-turbo (OpenAI) | `OPENAI_API_KEY` |

---

## ⚙️ 1. Setup Environment Variables

Set the following environment variables in your terminal or `.env` file:

### 🔓 For **Free Tier** (Fetch AI):

```bash
export LLM_TIER=free
export FETCH_API_KEY=your-fetch-api-key
```

### 🔐 For **Premium Tier** (OpenAI):

```bash
export LLM_TIER=premium
export OPENAI_API_KEY=your-openai-api-key
```

---

## 🚀 2. Run a Chatbot

You can test the auto-switching logic in a chatbot script.

### Example using GPT or Fetch AI:
```bash
python src/ai_agent/chatbot_ai.py
```

OR plug into any logic like:
```python
from llm_router import generate_response

messages = [
    {"role": "system", "content": "You are a helpful financial assistant."},
    {"role": "user", "content": "আমার বাবার একটি LIC আছে।"}
]

reply = generate_response(messages)
print("Bot:", reply)
```

---

## 🧪 3. Test Switch Logic

Change tiers like this:
```bash
export LLM_TIER=free   # Uses ASI1-mini
export LLM_TIER=premium  # Switches to GPT
```

---

## 📂 Files Used

| File                         | Purpose                            |
|------------------------------|------------------------------------|
| `llm_router.py`              | Backend switcher between LLMs      |
| `chatbot_ai.py`              | Chatbot using `generate_response()`|
| `contextual_prompt_loader.py`| Loads intro/followup/will prompts |
| `prompt_templates/`          | Contains .txt templates            |

---

## ❓ Need Help?

Contact the maintainer or check the issues tab.

