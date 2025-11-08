Skip to content
Navigation Menu
aryan7777
https-github.com-aryan7777-LLMCostEstimator

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
https-github.com-aryan7777-LLMCostEstimator
/
Name your file...
in
main

Edit

Preview
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
# AI Cost Calculator (Open Source)
# Created by Aryan — made for developers to estimate AI model usage cost easily.

# Price per 1K tokens (as of current public rates)
prices = {
    "gpt-4": 0.03,
    "claude": 0.003,
    "gemini": 0.002,
    "mistral": 0.001,
    "gpt-3.5": 0.0015,
    "command-r": 0.002
}

# Get user input
prompt = input("Paste your prompt: ")

# Simple word-based token estimation
words = prompt.split()
estimated_tokens = len(words) * 1.3  # Rough average (1 word ≈ 1.3 tokens)

print(f"\nEstimated tokens: {estimated_tokens:.0f}")

# Cost calculation
print("\n--- Estimated Cost per Model ---")
for model, price in prices.items():
    cost = (estimated_tokens / 1000) * price
    print(f"{model.upper()} cost: ${cost:.4f}")
    if cost > 0.50:
        print("⚠️  Warning: This might be expensive!")

print("\nMade
Paste your prompt: Explain quantum computing in simple terms

Estimated tokens: 78
--- Estimated Cost per Model ---
GPT-4 cost: $0.0023
CLAUDE cost: $0.0003
GEMINI cost: $0.0002
MISTRAL cost: $0.0001
COMMAND-R cost: $0.0002for open-source devs ❤️ | Free to use & modify")
New File at / · aryan7777/https-github.com-aryan7777-LLMCostEstimator
