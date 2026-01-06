# Smart Daily Commute Optimizer

## Summary
Smart Daily Commute Optimizer helps commuters in urban areas optimize their daily travel by predicting the best routes and estimating travel times based on real-time traffic data.

## Problem it Solves
Millions of people face daily stress and time loss due to traffic congestion and public transport delays, affecting punctuality, work-life balance, and mental well-being. This agent aims to alleviate these issues by providing real-time optimized travel solutions.

## How It Works
1. Users input their start and end locations.
2. The agent fetches real-time traffic data between the locations.
3. It calculates the optimal route and estimated time based on current conditions.
4. The user receives a suggested route with estimated travel time and traffic conditions.

## Example Use Case
A commuter entering their home and office addresses receives a route suggesting taking Highway A with an estimated travel time of 30 minutes, helping them avoid delays and plan better.

## How to Run
1. Clone the repository.
2. Install dependencies using Poetry: `poetry install`
3. Create a `.env` file from `.env.example` and add your API key.
4. Run the agent: `python agent.py <start_location> <end_location>`

## Tech Stack
- Python
- Pydantic
- LangGraph
- OpenAI
- Requests
- Flask
