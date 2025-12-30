# Smart Grocery Saver

## Summary
Smart Grocery Saver is an AI agent designed to optimize your grocery shopping by helping you stick to your budget, reduce food waste, and cater to your dietary preferences.

## Problem It Solves
Millions of families face challenges in managing grocery budgets and minimizing food waste. Smart Grocery Saver addresses these issues by providing an optimized shopping list and waste reduction tips tailored to your household's needs.

## How It Works
The agent takes inputs such as your budget, dietary preferences, household size, and current inventory. It processes this information to generate a shopping list that fits your budget and offers tips to minimize waste.

## Example Use Case
You input your monthly grocery budget of $300, specify a vegetarian preference, and list your current inventory. The agent returns a suggested shopping list within budget and offers tips on reducing food waste.

## How to Run It
1. Ensure you have Python 3.8 or higher installed.
2. Install dependencies using Poetry: `poetry install`
3. Run the agent with an input JSON file: `python agent.py input.json`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state machine management
- OpenAI for language processing
- Pandas for data manipulation
- Requests for external API calls
