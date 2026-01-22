import os
import sys
from dotenv import load_dotenv
from pydantic import ValidationError
from schemas import HydrationInput, HydrationOutput
from graph import HydrationStateMachine
from langchain_openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    print("Error: OPENAI_API_KEY is not set in environment variables.")
    sys.exit(1)

class SmartDailyHydrationCoach:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.llm = OpenAI(api_key=api_key)
        self.state_machine = HydrationStateMachine(self.llm)

    def start(self, user_input: dict):
        try:
            input_data = HydrationInput(**user_input)
            output = self.state_machine.run(input_data)
            print(output.json(indent=2))
        except ValidationError as e:
            print("Input validation error:", e)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python agent.py <weight_kg> <activity_level>")
        sys.exit(1)

    try:
        weight = float(sys.argv[1])
        activity_level = float(sys.argv[2])
        user_input = {
            "weight_kg": weight,
            "activity_level": activity_level
        }

        coach = SmartDailyHydrationCoach(api_key=API_KEY)
        coach.start(user_input)
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and activity level.")
        sys.exit(1)