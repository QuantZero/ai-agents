# Smart Home Maintenance Scheduler

## Summary
The Smart Home Maintenance Scheduler helps homeowners and renters efficiently manage and schedule routine home maintenance tasks to ensure safety and maintain home value.

## Problem It Solves
Homeowners and renters often forget regular maintenance tasks due to busy schedules, which can lead to safety hazards, costly repairs, or reduced home value. This agent provides a simple way to track and remind users of these tasks.

## How It Works
The agent takes a list of maintenance tasks, each with a name, frequency (in months), and last completed date. It calculates which tasks are due based on the current date and alerts the user to complete them.

## Example Use Case
A user inputs tasks such as checking smoke detectors every 6 months, cleaning gutters every 3 months, and servicing HVAC systems annually. The agent tracks these tasks and notifies the user when they are due.

## How to Run It
1. Set up your Python environment and install dependencies using Poetry.
2. Run the agent using: `python agent.py`
3. The agent will output which tasks are due for maintenance.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI (via langchain-openai) for potential future integration
- python-dotenv for environment variable management
