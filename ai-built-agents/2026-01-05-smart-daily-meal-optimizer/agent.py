import os
import sys
from dotenv import load_dotenv
from pydantic import ValidationError
from schemas import MealPlanInput, MealPlanOutput
from graph import MealOptimizerGraph

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    print("Error: OPENAI_API_KEY is not set in the environment variables.")
    sys.exit(1)

def main():
    try:
        user_input = input("Enter your dietary preferences and budget (e.g., vegetarian, $50 per week): ")
        meal_input = MealPlanInput.parse_raw(user_input)
        graph = MealOptimizerGraph(api_key=API_KEY)
        meal_plan = graph.run(meal_input)
        print("Here is your optimized meal plan:")
        print(MealPlanOutput.from_response(meal_plan))
    except ValidationError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()