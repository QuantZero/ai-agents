# Personal Safety Advisor

## Summary
The Personal Safety Advisor is an AI-powered agent that provides real-time safety information and advice for individuals concerned about personal safety, especially when traveling or commuting in urban environments.

## Problem It Solves
Millions of people are concerned about their personal safety when moving through unfamiliar or potentially risky areas. This agent helps users avoid risky situations by providing timely safety advice based on real-time data.

## How It Works
The agent takes a location name as input, retrieves its geographical coordinates, and fetches safety data for that location. It then uses an AI model to generate personalized safety advice based on current conditions.

## Example Use Case
A user traveling to a new city can input the destination area into the agent. The agent will provide tailored safety advice, such as avoiding certain areas at night due to higher crime rates or being cautious about traffic conditions.

## How to Run It
1. Clone the repository.
2. Set up your environment variables in a `.env` file (use `.env.example` as a guide).
3. Install dependencies using Poetry: `poetry install`
4. Run the agent: `python agent.py`

## Tech Stack Used
- **pydantic** for data validation and management
- **langgraph** for state management
- **OpenAI** for AI model integration
- **geopy** for geocoding location names
- **requests** for HTTP requests
