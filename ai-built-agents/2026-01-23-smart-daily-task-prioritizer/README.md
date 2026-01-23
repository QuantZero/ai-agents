# Smart Daily Task Prioritizer

## Summary
The Smart Daily Task Prioritizer is an AI agent that helps organize and prioritize daily tasks to enhance productivity and reduce stress.

## Problem it Solves
Many individuals struggle with managing their daily tasks efficiently, often leading to missed deadlines and increased stress. This agent assists in prioritizing tasks based on urgency and importance.

## How it Works
The agent accepts a list of tasks, each with a title, description, due date, and priority level. It then sorts and schedules these tasks, providing a prioritized list that optimizes the user's workflow.

## Example Use Case
A user provides a JSON file with tasks, and the agent outputs a JSON list of tasks sorted by priority and due date, ensuring critical tasks are addressed first.

## How to Run It
1. Ensure you have Python 3.8+ installed.
2. Install dependencies with `poetry install`.
3. Prepare a JSON file with tasks.
4. Run the agent with: `python agent.py <tasks.json>`

## Tech Stack
- Python
- Pydantic
- LangGraph
- OpenAI
- Python-dotenv
