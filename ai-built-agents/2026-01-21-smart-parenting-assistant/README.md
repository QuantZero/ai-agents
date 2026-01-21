# Smart Parenting Assistant

## Summary
The Smart Parenting Assistant is an AI-driven tool designed to help parents manage their children's daily routines, including meal planning, activity suggestions, and health tracking.

## Problem It Solves
Parents often face the challenge of organizing their children's daily activities, meals, and health considerations. The Smart Parenting Assistant simplifies this by providing personalized daily plans, reducing stress and improving family well-being.

## How It Works
The agent takes input about the child, such as name, age, preferences, and health information. It then uses AI to generate a daily plan that includes a meal suggestion, an activity recommendation, and any relevant health advice.

## Example Use Case
A parent inputs their child's preferences and health information into the system. The agent returns a vegetarian meal plan, suggests an outdoor activity, and advises avoiding peanuts due to an allergy.

## How to Run It
1. Ensure you have Python 3.8+ installed.
2. Install dependencies using Poetry: `poetry install`.
3. Set your OpenAI API key in a `.env` file.
4. Run the agent with `python agent.py`.

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for AI capabilities
- Python-dotenv for environment management
