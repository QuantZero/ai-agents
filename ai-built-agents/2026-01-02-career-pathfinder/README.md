# Career Pathfinder

## Summary
Career Pathfinder is an AI agent designed to help individuals identify and pursue career paths that align with their skills, interests, and the ever-changing job market.

## Problem it Solves
Millions of individuals, especially recent graduates and mid-career professionals, struggle to identify and pursue career paths that align with their skills, interests, and the job market. This challenge leads to career dissatisfaction, underemployment, and wasted potential.

## How it Works
The agent takes input regarding an individual's skills, interests, and current job (if applicable) and uses AI to recommend suitable career paths. It considers current job market trends and provides a rationale for each recommendation.

## Example Use Case
A recent graduate inputs their skills and interests into the system and receives a list of recommended career paths, such as "Data Scientist" or "Product Manager," along with reasons why these paths are suitable.

## How to Run It
1. Ensure you have Python 3.8+ installed.
2. Clone the repository.
3. Install dependencies using Poetry: `poetry install`
4. Set your OpenAI API key in a `.env` file.
5. Run the agent: `python agent.py < input.json`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI API for intelligence
- Dotenv for environment variable management
