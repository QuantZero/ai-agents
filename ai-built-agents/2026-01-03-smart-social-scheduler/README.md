# Smart Social Scheduler

## Summary
The Smart Social Scheduler is an AI agent designed to help coordinate social events by suggesting optimal times based on the participants' schedules.

## Problem it Solves
Many people struggle with coordinating social events due to differing schedules, leading to missed opportunities for connection and increased feelings of isolation. This agent aims to alleviate this issue by providing intelligent suggestions for meeting times that work for all participants.

## How it Works
The agent takes input in the form of a JSON payload containing user email, friend emails, preferred days, and time slots. It uses calendar integration to fetch availabilities and suggests events. It then notifies users with the suggestions via email or SMS.

## Example Use Case
A working professional wants to organize a weekend brunch with friends but finds it hard to agree on a time. The Smart Social Scheduler helps by analyzing everyone's schedules and suggesting the best time slots for all involved.

## How to Run It
1. Set up your environment variables using the `.env.example` file.
2. Run the script with proper input: `python agent.py '{"user_email": "user@example.com", "friend_emails": ["friend1@example.com", "friend2@example.com"], "preferred_days": ["Saturday", "Sunday"], "time_slots": ["18:00-20:00", "20:00-22:00"]}'`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state machine management
- OpenAI API for conversational logic
- Calendar and Communication APIs
