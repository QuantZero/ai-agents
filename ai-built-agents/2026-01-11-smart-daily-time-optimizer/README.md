# Smart Daily Time Optimizer

## Summary
Smart Daily Time Optimizer is an AI agent designed to help individuals manage their daily schedules more effectively, reducing stress and improving work-life balance.

## Problem It Solves
Many people struggle with time management, leading to inefficient work habits and stress. This agent optimizes daily schedules by prioritizing tasks based on importance and available time.

## How It Works
The agent receives a list of tasks with their durations and importance levels. It uses a state machine to prioritize tasks and fit them into the available time, returning an optimized schedule.

## Example Use Case
- A busy professional inputs their tasks for the day along with the available hours. The agent returns a schedule that maximizes productivity by focusing on the most important tasks.

## How to Run It
1. Set environment variables as per `.env.example`.
2. Install dependencies with `poetry install`.
3. Run the application using `uvicorn agent:app --reload`.
4. Send POST requests to `/optimize` with your schedule data.

## Tech Stack
- **Python** for scripting
- **FastAPI** for API management
- **Pydantic** for data validation
- **LangGraph** for state machine management
- **OpenAI** (via langchain-openai) for potential AI enhancements
- **APScheduler** for scheduling tasks
