# Daily Stress Manager

## Summary
Daily Stress Manager is an AI agent designed to help individuals manage their daily stress by providing personalized advice based on user input.

## Problem it Solves
Millions of people experience daily stress, which can lead to health issues and decreased quality of life. This agent helps users identify stress triggers and offers practical strategies for stress management.

## How it Works
Users input their stressors and current stress level. The agent uses the OpenAI API to generate personalized advice on managing stress. This advice is delivered back to the user in an easily digestible format.

## Example Use Case
A user feeling overwhelmed at work inputs "work deadlines" as their stressor and rates their stress level as "7". The agent responds with advice such as time management tips and relaxation techniques.

## How to Run It
1. Clone the repository.
2. Install dependencies using `poetry install`.
3. Set the `OPENAI_API_KEY` in your environment variables.
4. Run the agent using `python agent.py <stressors> <stress_level>`.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI API for generating advice
- dotenv for environment variable management