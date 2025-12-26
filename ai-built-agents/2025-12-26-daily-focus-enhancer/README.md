# Daily Focus Enhancer

## Summary
The Daily Focus Enhancer is an AI agent designed to help individuals improve their focus and productivity by analyzing their tasks and current focus challenges, and providing actionable advice.

## Problem Solved
Millions struggle with maintaining focus at work or during study due to distractions and poorly optimized schedules, leading to decreased productivity and increased stress.

## How It Works
The agent takes user input about their current tasks and focus challenges, processes this information through a state machine powered by a language model, and returns practical advice to improve focus.

## Example Use Case
A user inputs their list of tasks for the day along with their current focus struggles (e.g., "too many meetings, constant email notifications"), and the agent provides customized advice on how to structure their day for better focus.

## How to Run
1. Clone the repository.
2. Create a `.env` file with your OpenAI API key.
3. Run `python agent.py` and follow the prompts.

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for language model interaction
- Python-dotenv for environment variable management
