# Smart Home Energy Optimizer

## Summary

Smart Home Energy Optimizer is an AI agent designed to help homeowners and renters reduce energy costs and minimize their environmental impact by providing actionable recommendations for optimizing energy usage.

## Problem It Solves

Millions of people face high energy bills and environmental concerns due to inefficient energy usage in their homes. Managing energy consumption manually is complex and time-consuming, often leading to unnecessary expenses and a higher carbon footprint.

## How It Works

The agent connects to your smart home devices using the Home Assistant API to gather data on current temperature and energy prices. It uses OpenAI's language model to analyze this data and provide energy optimization recommendations that can help reduce your energy costs and environmental impact.

## Example Use Case

A homeowner can run the agent to receive personalized recommendations on when to run appliances, adjust thermostats, or change energy providers based on real-time data, thereby saving on energy bills and reducing carbon emissions.

## How to Run It

1. Clone the repository.
2. Install dependencies using `poetry install`.
3. Set up your `.env` file based on `.env.example`.
4. Run the agent using `python agent.py`.

## Tech Stack Used

- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for generating recommendations
- Home Assistant API for smart home integration
- Numpy and Pandas for data manipulation
