# 💰 Wealth_report_Agent + Digital_will 

A 🇧🇩 Bengali-first AI tool to organize family wealth, track assets, and simplify inheritance planning.

## 🧩 Problem
Bengali families often have financial assets scattered across LIC, PF, gold, SIPs, FDs, land, loans, and banks — with no centralized documentation.

## 💡 Solution
**WealthReportBDAI** is an AI-powered assistant that:
- ✅ Gathers asset info via chat
- 📊 Generates a secure, categorized Wealth Report
- ⏰ Sends reminders
- 📜 Helps draft digital will instructions
- 🧾 Offers nominee alerts & guidance

## 🧠 Tech Stack
- React Native / Flutter frontend
- Firebase / Supabase backend
- LangChain + GPT AI layer
- AES-256 encryption

## 📦 Asset Schema
See `/docs/asset_schema.json`

## 🚀 Roadmap
- [ ] Chatbot intake
- [ ] Wealth report
- [ ] Digital will
- [ ] Nominee alerts

## 🙌 Contributing
PRs and feedback welcome!

🆘 Support
For issues or questions:
Check the troubleshooting section
Review the GitHub issues
Create a new issue with detailed information

📁 Project Structure
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
│   ├── backend/                # Flask/Firebase backend logic
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



Component	Reason to Include
README.md   Explains what the project is and how to use it.
LICENSE	    Tells others how they can use/contribute to my code.
.gitignore  Prevents unnecessary clutter.
docs/	    Clearly separates all design assets, schemas, and API plans.
data/	    Sample input/output to make my repo testable and demonstrable.
src/        Clean modular code structure; separates AI, backend, frontend, utils.
tests/	    Test files for building confidence for contributors and CI/CD pipelines.
config/	    Useful for environment toggles and secure credentials.

👨‍💻 Author
Saqeb Newaz 

Made with 💚 by Saqeb Newaz for the Bengali 🇧🇩 community
