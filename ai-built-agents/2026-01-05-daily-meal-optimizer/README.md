# Daily Meal Optimizer

## Summary
The Daily Meal Optimizer is an AI agent that helps individuals and families plan nutritious meals within their budget, reducing stress and improving eating habits.

## Problem It Solves
Many people struggle with planning daily meals that are both nutritious and budget-friendly. This often leads to unhealthy eating habits and increased stress. This agent provides a solution to create meal plans based on user preferences and budgets.

## How It Works
Users provide their dietary preferences and budget. The AI agent then generates a meal plan tailored to these inputs, ensuring meals are nutritious and cost-effective. It uses OpenAI's language model to understand user requirements and craft suitable meal plans.

## Example Use Case
A user inputs "vegetarian, $50 per week" into the system. The agent processes this information and returns a meal plan that meets these criteria, such as including dishes like "Grilled tofu salad" and "Vegetarian chili."

## How to Run It
1. Clone the repository.
2. Ensure you have Python 3.8 or newer installed.
3. Install dependencies using `pip install -r requirements.txt` or `poetry install`.
4. Set your OpenAI API key in a `.env` file (use `.env.example` for reference).
5. Run the agent using `python agent.py` and follow the prompts.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for flow management
- OpenAI for language processing
- Python-dotenv for environment variable management