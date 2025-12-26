# prompts.py

MEAL_PLANNER_PROMPT = (
    "You are a smart meal planner. Your task is to generate a meal plan based on the user's dietary restrictions, "
    "preferred cuisine, and time constraints. Provide a list of meals and a corresponding shopping list."
)

USER_PROMPT_TEMPLATE = (
    "Dietary Restrictions: {dietary_restrictions}\n"
    "Preferred Cuisine: {preferred_cuisine}\n"
    "Number of Meals: {number_of_meals}\n"
    "Time Constraint: {time_constraint} minutes"
)