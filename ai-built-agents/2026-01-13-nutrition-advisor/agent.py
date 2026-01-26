import os
import sys
import openai
from dotenv import load_dotenv
from langgraph import StateMachine
from pydantic import BaseModel, ValidationError
from typing import Optional

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

class UserInput(BaseModel):
    age: int
    weight: float
    height: float
    activity_level: str
    dietary_preferences: Optional[str] = None

class NutritionAdvice(BaseModel):
    advice: str

class NutritionStateMachine(StateMachine):
    def __init__(self):
        super().__init__()

    def start(self, user_input: UserInput) -> NutritionAdvice:
        # Process user input and generate nutritional advice
        prompt = self.create_prompt(user_input)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        advice = response.choices[0].text.strip()
        return NutritionAdvice(advice=advice)

    def create_prompt(self, user_input: UserInput) -> str:
        return (f"Provide personalized dietary advice for a {user_input.age} year old "
                f"with a weight of {user_input.weight} kg, height of {user_input.height} cm, "
                f"and an activity level of {user_input.activity_level}. "
                f"Dietary preferences: {user_input.dietary_preferences or 'none'}.")


def main():
    try:
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        activity_level = input("Enter your activity level (e.g., sedentary, active): ")
        dietary_preferences = input("Enter any dietary preferences (or press Enter for none): ") or None

        user_input = UserInput(
            age=age,
            weight=weight,
            height=height,
            activity_level=activity_level,
            dietary_preferences=dietary_preferences
        )

        machine = NutritionStateMachine()
        advice = machine.start(user_input)
        print("\nYour personalized nutritional advice:")
        print(advice.advice)

    except ValidationError as e:
        print("Input validation error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
