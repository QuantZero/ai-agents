# Smart Meal Planner

## Summary
Smart Meal Planner is an intelligent agent designed to help individuals and families plan nutritious meals effortlessly, taking into consideration dietary restrictions, preferred cuisine, and time constraints.

## Problem It Solves
Many people struggle with planning meals due to time constraints, dietary needs, and lack of culinary inspiration, which often leads to unhealthy eating habits and stress. This agent offers a solution by providing tailored meal plans and shopping lists.

## How It Works
The agent uses a combination of user inputs and an AI model to generate meal plans. Users provide dietary restrictions, preferred cuisine, number of meals, and time constraints. The agent then processes this information to output a personalized meal plan and shopping list.

## Example Use Case
A user inputs their preference for vegetarian meals, a Mediterranean cuisine, three meals for the day, and a time constraint of 30 minutes per meal. The agent outputs a meal plan with corresponding recipes and a shopping list.

## How to Run It
1. Clone the repository.
2. Ensure Python 3.8 or higher is installed.
3. Install dependencies using `poetry install`.
4. Run the agent with `python agent.py '{"dietary_restrictions": ["vegetarian"], "preferred_cuisine": "Mediterranean", "number_of_meals": 3, "time_constraint": 30}'`

## Tech Stack
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for AI capabilities
- Python-dotenv for environment variable management