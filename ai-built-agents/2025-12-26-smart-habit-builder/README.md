# Smart Habit Builder

## Summary
The Smart Habit Builder is an AI-driven agent designed to assist users in forming and maintaining healthy habits to enhance wellness and productivity.

## Problem It Solves
Millions struggle with habit formation due to lack of motivation, poor personalization, or overwhelm. This agent provides a structured approach to habit building, making it easier and more personalized.

## How It Works
The agent uses a state machine to guide users through the habit formation process, providing encouragement and tracking progress daily. Users input the habit they wish to develop and the desired duration, and the agent handles the rest.

## Example Use Case
A user wants to develop a daily exercise habit. They input "exercise" as the habit name and "30" days as the duration. The agent guides them through each day, providing motivation and tracking their progress until the habit is established.

## How to Run It
1. Clone the repository.
2. Install dependencies using Poetry: `poetry install`
3. Run the agent: `python agent.py`
4. Follow prompts to input desired habit and duration.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state machine management
- Langchain-OpenAI for potential future enhancements
- Python-dotenv for environment variable management
