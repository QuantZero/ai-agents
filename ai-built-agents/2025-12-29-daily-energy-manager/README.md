# Daily Energy Manager

## Summary
Daily Energy Manager is an AI agent that helps individuals manage their energy levels throughout the day by providing tailored recommendations for work, rest, and energizing activities.

## Problem it Solves
Millions of people experience fluctuations in their energy levels, leading to decreased productivity and increased stress. This agent offers personalized advice based on individual energy patterns to enhance productivity and well-being.

## How it Works
The agent collects data about a user's energy levels and preferences, analyzes this information, and generates a schedule optimized for maintaining high productivity and reducing stress. It uses OpenAI's language model to generate natural language recommendations.

## Example Use Case
A user can input their wake time and receive a schedule that outlines optimal times for focused work, breaks, and activities to boost energy.

## How to Run It
1. Ensure you have Python 3.8 or higher installed.
2. Clone the repository.
3. Install dependencies using Poetry: `poetry install`
4. Set your OpenAI API key in a `.env` file.
5. Run the agent: `python agent.py <user_id> <wake_time>`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for natural language processing
- Python-dotenv for environment variable management
