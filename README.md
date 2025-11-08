# https-github.com-aryan7777-LLMCostEstimator
LLMCostEstimator  Description: something like “Estimate AI prompt cost across GPT, Claude, Gemini &amp; more 💸”
# 🧮 OpenAI Cost Estimator

A simple, open-source Python tool that helps developers estimate the **token usage and cost** of prompts for different AI models like GPT-4, Claude, and others before sending them to the API.

---

## 🚀 Features

- Calculates **estimated tokens** based on your prompt length  
- Shows **cost per model** (GPT-4, Claude, etc.)  
- Gives a **warning** if your prompt is expensive  
- Fully **CLI-based** — works right inside **Termux, Linux, or macOS Terminal**

---

## 🛠️ Installation

Clone the repo and run the script:

```bash
git clone https://github.com/yourusername/openai-cost-estimator.git
cd openai-cost-estimator
python3 cost_estimator.py
Paste your prompt: Explain quantum computing in simple terms.
Tokens: 65.0
GPT-4 cost: $0.00195
Claude cost: $0.000195
WARNING: This is expensive!
---

Would you like me to tweak it so it includes **OpenAI, Claude, Gemini, and Mistral prices** in the table too?
