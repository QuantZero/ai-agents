# Exercise Companion

## Summary
The Exercise Companion is an AI-powered agent designed to help individuals maintain a consistent exercise routine by providing personalized exercise plans, motivational tips, and progress tracking.

## Problem It Solves
Many people struggle to maintain a consistent exercise routine due to a lack of personalized guidance, motivation, and adjustment based on progress. This agent addresses these issues by offering tailored exercise plans and motivational support.

## How It Works
The agent uses input about the user's fitness level, goals, and preferences to create a personalized exercise plan. It uses OpenAI's capabilities to generate motivational tips and suggestions to keep the user engaged and on track.

## Example Use Case
A user inputs their current fitness level, goals, and exercise preferences. The agent generates a personalized workout plan and offers weekly motivational messages to help the user stay committed to their fitness journey.

## How to Run It
1. Ensure you have Python 3.8+ installed.
2. Clone this repository.
3. Install dependencies using `poetry install`.
4. Create a `.env` file with your OpenAI API key.
5. Run the agent with `python agent.py '<user_input_json>'`.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for AI-driven responses
- Python-dotenv for environment variable management
