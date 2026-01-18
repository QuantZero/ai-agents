# Smart Daily Expense Optimizer

## Summary
The Smart Daily Expense Optimizer is an AI-driven tool designed to help individuals manage their daily expenses more effectively and achieve their savings goals.

## Problem It Solves
Many people face challenges in managing their finances due to fluctuating expenses and unexpected costs. This tool provides a structured way to track expenses and optimize spending, thereby reducing financial stress and aiding in savings.

## How It Works
The agent takes input of income, fixed and variable expenses, and savings goals. It calculates total expenses, provides a remaining budget after accounting for savings, and offers advice on financial management.

## Example Use Case
A user with a monthly income of $3000, fixed expenses (rent, utilities) of $1200, variable expenses (groceries, entertainment) of $450, and a savings goal of $500 uses this tool. The agent calculates the total expenses, remaining budget, and offers personalized advice.

## How to Run It
1. Clone the repository.
2. Set up your environment variables in a `.env` file as shown in the `.env.example`.
3. Install dependencies using `poetry install`.
4. Run the agent with `python agent.py`.

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state machine
- OpenAI API for intelligence
- Python-dotenv for environment variable management
