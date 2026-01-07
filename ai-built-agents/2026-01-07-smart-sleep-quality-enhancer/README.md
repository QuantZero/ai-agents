# Smart Sleep Quality Enhancer

## Summary
The Smart Sleep Quality Enhancer is an AI agent designed to improve your sleep quality by providing personalized suggestions based on your current sleep patterns, stress levels, and environmental factors.

## Problem It Solves
Millions of people suffer from poor sleep quality due to various factors such as stress, irregular sleep environments, and inconsistent routines. This agent aims to address these issues by offering actionable advice to enhance your sleep.

## How It Works
The agent uses input from the user regarding their sleep duration, stress level, and environmental noise level. It then processes this information through a decision graph to generate personalized sleep improvement suggestions.

## Example Use Case
A user with a sleep duration of 6 hours, a stress level of 8, and an environment noise level of 7 would receive suggestions such as using a white noise machine or engaging in meditation before bed.

## How to Run It
1. Clone the repository.
2. Install dependencies with `poetry install`.
3. Set the `OPENAI_API_KEY` in your environment.
4. Run the agent script with `python agent.py`.

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI API for processing
- Python-dotenv for environment variable management
