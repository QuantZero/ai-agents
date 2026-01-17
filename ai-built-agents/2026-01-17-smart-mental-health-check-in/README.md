# Smart Mental Health Check-In

## Summary
Smart Mental Health Check-In is an AI agent designed to assist individuals in managing their mental health through daily check-ins and emotional support.

## Problem it Solves
Millions of people face mental health challenges, often feeling overwhelmed by stress and anxiety. This agent provides a supportive tool for users to check in daily and receive empathetic responses to help manage their emotional well-being.

## How It Works
The agent uses AI to process user input and provide a supportive response. Users input their thoughts or feelings, and the agent responds with empathy and potential advice, assisting with mental health management.

## Example Use Case
A user feeling stressed after a long day could input their feelings into the agent and receive a supportive response that helps them reflect and manage their emotions better.

## How to Run
1. Set your OpenAI API key in an environment variable `OPENAI_API_KEY`.
2. Install dependencies using Poetry: `poetry install`
3. Run the agent: `python agent.py '<your_check_in_text>'`

## Tech Stack Used
- Python
- Pydantic
- LangGraph
- OpenAI
- Python-dotenv
