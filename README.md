**Oitijhho AI | ঐতিহ্য AI | HeritageAI**

## 💰 Wealth_report_Agent + Digital_will_creator  

A 🇧🇩 Bengali-first AI tool to organize family wealth, track assets, and simplify inheritance planning — so families aren’t left in the dark during times of grief.

---

## 🧩 Problem

In many Bengali families, financial assets are fragmented across LICs, PFs, gold, SIPs, FDs, land, loans, and bank accounts — usually with little to no centralized documentation. Often, only one person knows the full picture. When that person passes away, others are left struggling.

This project was inspired by personal hardship — when our family lost our father in 2017. My mother, sister (then with a newborn in the UK), and I (based in Canada) had to navigate inheritance paperwork, nominee forms, and power of attorney signatures while dealing with grief and uncertainty. The goal is to ensure no one else has to face that confusion, inshaAllah.

---

## 💡 Solution

**Oitijhho AI | ঐতিহ্য AI** is an AI-powered assistant (translates to **HeritageAI**) that:

- ✅ Gathers asset information via chat
- 📊 Generates a categorized and secure Wealth Report
- 🔐 Offers AES-256 encryption for sensitive data
- 📜 Helps draft digital will guidance
- ⏰ Sends reminders for expiring investments and follow-ups
- 🧾 Sends nominee alerts and offers legal guidance

---

## 🧠 Tech Stack

| Tier        | Technology                               |
|-------------|------------------------------------------|
| Free        | Fetch API + rule-based mini-agent        |
| Premium     | GPT (OpenAI's best-fit model via LangChain) |
| Frontend    | React Native / Flutter                   |
| Backend     | Flask / Firebase / Supabase              |
| Security    | AES-256 encryption                       |

## 📊 Competitive Landscape

| Feature                    | Oitijhho AI      | Local Legal Firms | Global Legacy Tools |
|----------------------------|------------------|-------------------|----------------------|
| Bengali Language Support   | ✅ Yes            | ⚠️ Partial         | ❌ None              |
| LIC / Khatiyan Integration | ✅ Yes            | ❌ No              | ❌ No                |
| AI-Powered Chat Intake     | ✅ Yes            | ❌ No              | ✅ Yes (Generic)     |
| Digital Will Assistance    | ✅ Yes            | ⚠️ Manual          | ✅ Yes               |
| Family-Friendly UX         | ✅ Yes            | ❌ No              | ⚠️ Often Complex     |
| Designed for Bangladesh    | ✅ Yes            | ✅ Yes             | ❌ No                |
| Diaspora Support (Canada, UK, etc.) | ✅ Yes    | ⚠️ Difficult       | ⚠️ Limited           |
| Crypto & bKash Wallets     | ✅ Yes            | ❌ No              | ⚠️ Some              |

> 💬 Verdict: **No existing solution currently combines AI-powered chat, inheritance planning, Bengali asset types, and diaspora support — built from real loss, for real families.**



## 📦 Asset Schema
See `/docs/asset_schema.json` for examples on: 
- LIC (Life Insurance)
- PF (Provident Fund)
- FDR / SIPs / Mutual Funds
- Khatiyan (Land Deeds)
- Gold / Jewelry / Crypto
- Cash / Bank Balances
- Loans / Bonds / Vehicles

---

## 🚀 Roadmap
- [x] Asset schema templates
- [x] Sample CSV input/output
- [ ] Chatbot intake via Fetch API
- [ ] Wealth report generator
- [ ] Digital will assistant
- [ ] Nominee alerts engine
- [ ] PWA Mobile deployment

---

## 🙌 Contributing
PRs and feedback welcome! If you're a developer, legal/finance expert, or someone passionate about building for families in South Asia, please join the journey.

## 🆘 Support
For issues or questions:
Check the troubleshooting section
Review the GitHub issues
Create a new issue with detailed information

## 📁 Project Structure - Preview in the Code TAB for correct formatting
wealthreportBDAI/
│
├── README.md
├── LICENSE
├── .gitignore
├── CONTRIBUTING.md 
│
├── docs/                       # Documentation files
│   └── asset_schema.json       # JSON structure for asset tracking
│
├── data/                       # Sample input/output data for testing
│   ├── sample_input.json
│   └── sample_output.json
│
├── src/                        # Source code
│   ├── ai_agent/               # AI logic (LLM, prompts, LangChain)
│   │   ├── prompt_templates/
│   │   └── asset_extractor.py
│   │
│   ├── backend/                # Flask/Firebase/Ngrok backend logic
│   │   ├── api.py
│   │   └── reminders.py
│   │
│   ├── frontend/               # React Native or Flutter frontend
│   │   ├── App.tsx (or main.dart)
│   │   ├── screens/
│   │   └── components/
│   │
│   └── utils/                  # Helper scripts (encryption, validation)
│       ├── encryption.py
│       └── date_parser.py
│
├── tests/                      # Unit tests
│   ├── test_asset_parser.py
│   └── test_reminder_engine.py
│
└── config/                     # App configurations
    ├── settings.dev.json
    └── firebase_config.json


**Why this layout?**
| Component     | Purpose                                              |
|---------------|------------------------------------------------------|
| `README.md`   | Project overview                                     |
| `docs/`       | Design, schema, API planning                         |
| `data/`       | Test cases and inputs                                |
| `src/`        | Source code: AI, backend, frontend, utils            |
| `tests/`      | Unit tests for CI/CD confidence                      |
| `config/`     | Local settings and environment management            |
| `.gitignore/` | Prevents unnecessary clutter                         |
| `LICENSE/`    | Tells others how they can use/contribute to my code |  


## 👨‍💻 Author
**Saqeb Newaz** 
Built with 💚 for the Bengali 🇧🇩 community, and for families like mine who had to navigate loss the hard way.
