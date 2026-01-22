# Smart Daily Hydration Coach

## Summary
The Smart Daily Hydration Coach is an AI agent designed to help individuals maintain proper hydration by recommending daily water intake based on personal weight and activity level.

## Problem It Solves
Millions of people struggle with maintaining proper hydration, leading to issues like fatigue, headaches, and decreased cognitive function. This agent provides personalized recommendations to encourage better hydration habits.

## How It Works
The agent uses user-provided weight and activity level to calculate an appropriate daily water intake recommendation. It leverages a language model to process inputs and generate suggestions.

## Example Use Case
A busy professional inputs their weight and activity level into the agent. The agent calculates and recommends the optimal amount of water they should drink daily to stay properly hydrated.

## How to Run It
1. Clone the repository.
2. Install dependencies using Poetry: `poetry install`
3. Create a `.env` file based on `.env.example` and set the `OPENAI_API_KEY`.
4. Run the agent via command line: `python agent.py <weight_kg> <activity_level>`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for language processing
- Python-dotenv for environment variable management