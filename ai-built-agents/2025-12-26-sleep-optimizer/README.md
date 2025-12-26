# Sleep Optimizer

## Summary
The Sleep Optimizer is an AI agent that helps users identify and improve factors affecting their sleep quality, leading to better health and productivity.

## Problem it Solves
Poor sleep affects millions, leading to issues like fatigue, reduced productivity, and health problems. Many struggle to identify the causes of their sleep issues, needing guidance to improve their sleep quality.

## How it Works
The agent uses user-provided data about sleep habits, stress levels, caffeine intake, and exercise frequency to generate personalized recommendations to improve sleep quality. It leverages OpenAI's language model for natural language understanding and recommendation generation.

## Example Use Case
A user inputs: 6.5 hours of sleep, poor sleep quality, high stress level, moderate caffeine intake, and low exercise frequency. The agent analyzes these inputs and provides actionable recommendations to help improve sleep quality.

## How to Run It
1. Ensure you have Python 3.8+ installed.
2. Clone the repository.
3. Install dependencies using Poetry: `poetry install`
4. Set your OpenAI API key in a `.env` file based on `.env.example`.
5. Run the agent: `python agent.py`

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for natural language processing
- Python-dotenv for environment variable management
