# 🦖 Dino Telegram Support Bot

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

An AI-powered Telegram bot that handles support queries during offline periods using Azure OpenAI.

---

## ✨ Features

* **Smart Message Classification** — Detects urgent vs. regular queries
* **Automated Responses** — Uses Azure OpenAI GPT-4 for intelligent replies
* **Conversation Tracking** — Stores all interactions in an SQLite database
* **Priority Handling** — Different workflows based on message urgency
* **Markdown Support** — Beautifully formatted responses in Telegram

---

## 📦 Prerequisites

* Python 3.8+
* [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) resource
* Telegram Bot Token from [@BotFather](https://t.me/BotFather)

---

## 🚀 Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/dino-bot.git
cd dino-bot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

```bash
cp .env.example .env
# Then open `.env` and edit with your credentials
```

4. **Run the bot**

```bash
python main.py
```

---

## 🔧 Configuration

Edit the `Config.py` file:

```ini
# Telegram
TELEGRAM_TOKEN=your_bot_token_here

# Azure OpenAI
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_API_BASE=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
```

---

## 📂 Project Structure

```
dino-bot/
├── main.py                # Entry point
├── config.py              # Configuration loader
├── handlers/              # Telegram message handlers
│   └── telegram_handler.py
├── services/              # Core services
│   ├── gpt_client.py      # OpenAI integration
│   ├── classifier.py      # Message classification
│   └── db_service.py      # Database operations
├── models/                # Data models
│   └── ticket_model.py    # DB schema
├── data/                  # Knowledge base
│   └── faqs.md            # Support content
└── logs/                  # Application logs
```

---

## 🤖 Example Interaction

**User:**

> I can't login to my account!

**Bot:**

```
🔧 This appears to be a technical issue. Try these steps:

• Visit our password reset page  
• Check your email for the reset link  
• If it persists, we'll review after Dec 15.
```

---

## 🛠 Troubleshooting

| Issue                 | Solution                       |
| --------------------- | ------------------------------ |
| API connection errors | Verify Azure credentials       |
| Database issues       | Check SQLite file permissions  |
| Message not processed | Review your Telegram bot token |

---

## 📄 License

Rjouba LCS
