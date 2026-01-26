
# Daily Task Scheduler

## Summary
The Daily Task Scheduler is an AI agent designed to help users manage their daily tasks efficiently, reducing stress and increasing productivity by dynamically adjusting schedules based on task input.

## Problem It Solves
Many people struggle with managing their daily tasks efficiently, leading to stress and decreased productivity. This agent helps users prioritize and adjust their tasks seamlessly.

## How It Works
The agent uses a state machine to manage tasks through different phases: Planning, In Progress, and Completed. It takes task descriptions and estimated times as inputs, plans the schedule, and transitions tasks through states.

## Example Use Case
A user inputs a task "Write report" with an estimated time of 120 minutes. The agent plans the task, starts it, and marks it as completed, adjusting the user's schedule as needed.

## How to Run It
1. Clone the repository.
2. Install dependencies using Poetry: `poetry install`
3. Run the agent with a task description and estimated time: `python agent.py "Write report" 120`

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- dotenv for environment variable management
