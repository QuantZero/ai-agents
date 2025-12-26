# Smart Budget Buddy

## Summary
Smart Budget Buddy is an AI-powered tool designed to help individuals manage their personal finances by providing personalized budget recommendations based on their income and expenses.

## Problem It Solves
Millions of people face challenges in managing their finances effectively, leading to stress and financial instability. Smart Budget Buddy helps users by offering actionable insights into their spending habits, promoting healthier financial decisions.

## How It Works
The agent takes input in the form of monthly income and a breakdown of expenses. It processes this data through a predefined state graph, generating budget recommendations that optimize savings and suggest potential areas for cost-cutting.

## Example Use Case
A user inputs a monthly income of $3000 and expenses such as rent=$1000, groceries=$500, and utilities=$200. The agent processes this information and suggests ways to allocate remaining funds towards savings or additional expenditures.

## How to Run It
1. Clone the repository.
2. Set up a virtual environment and install dependencies using `poetry install`.
3. Run the agent using: `python agent.py <income> <expenses>`

Example: `python agent.py 3000 rent=1000 groceries=500 utilities=200`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI capabilities for response generation
