# Nutrition Advisor

## Summary
Nutrition Advisor is an AI agent designed to provide personalized dietary advice, helping individuals make healthier food choices effortlessly.

## Problem it Solves
Millions of people struggle with maintaining a balanced diet due to busy lifestyles, leading to health issues like obesity and malnutrition. This agent targets individuals seeking to improve their eating habits and overall health by providing tailored nutritional guidance.

## How it Works
The agent takes user inputs such as age, weight, height, activity level, and dietary preferences. It then generates personalized dietary advice using OpenAI's language model.

## Example Use Case
A user enters their age, weight, height, activity level, and dietary preferences into the system. The agent processes this information and returns customized nutritional advice, aiding the user in making healthier food choices.

## How to Run It
1. Clone the repository.
2. Install dependencies using `poetry install`.
3. Set up your environment variables as detailed in the `.env.example`.
4. Run the agent with `python agent.py`.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI API for generating advice
- Python-dotenv for environment variable management
