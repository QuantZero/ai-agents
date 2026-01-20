# Smart Home Energy Saver

## Summary
The Smart Home Energy Saver is an AI agent designed to help homeowners and renters reduce energy costs and minimize their carbon footprint by providing customized energy-saving tips.

## Problem it Solves
With rising energy costs and environmental concerns, efficiently managing home energy usage is a challenge many households face. This agent addresses the need for practical advice tailored to individual household needs.

## How It Works
The agent collects basic information about the user's home, such as size, number of occupants, and current energy rate. It then uses this information, in conjunction with AI, to provide personalized energy-saving suggestions.

## Example Use Case
A family of four living in a 2,000 square foot home can enter their details and receive tips on how to adjust their thermostat settings, optimize appliance usage, and identify potential areas for energy savings.

## How to Run It
1. Clone the repository.
2. Set up your environment variables in a `.env` file (see `.env.example`).
3. Install dependencies using `poetry install`.
4. Run the agent with `python agent.py` and follow the prompts.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for generating energy-saving insights
- Dotenv for environment variable management