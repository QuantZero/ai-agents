# Disaster Preparedness Planner

## Summary
The Disaster Preparedness Planner is an AI agent designed to help individuals and families prepare for natural disasters by providing location-based preparedness guides.

## Problem It Solves
Millions of people live in areas prone to natural disasters such as hurricanes, earthquakes, and floods. Many are unprepared due to a lack of knowledge or time, leading to chaos and increased risk during emergencies.

## How It Works
Users provide their address, and the agent uses geolocation services to determine their exact location. It then provides a disaster preparedness guide tailored to their area.

## Example Use Case
A family living in a hurricane-prone area inputs their address into the agent. The agent returns a guide with specific recommendations for hurricane preparedness, such as evacuation routes and emergency supply checklists.

## How to Run It
1. Clone the repository
2. Install dependencies using `poetry install`
3. Run the agent using: `python agent.py <address>`

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- Geopy for geolocation
- dotenv for environment variable management