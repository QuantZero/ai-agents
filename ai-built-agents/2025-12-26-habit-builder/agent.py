# agent.py

import os
import sys
import logging
from dotenv import load_dotenv
from langgraph import Agent
from schemas import UserInput, HabitState
from graph import HabitBuilderGraph

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class SmartHabitBuilder:
    def __init__(self):
        self.agent = Agent(
            graph=HabitBuilderGraph(),
            initial_state=HabitState()  
        )

    def run(self, user_input: UserInput):
        try:
            logger.info("Starting the habit-building process.")
            response = self.agent.run(user_input.dict())
            logger.info("Process completed successfully.")
            return response
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            sys.exit(1)


def main():
    user_input = UserInput.parse_obj({
        'habit_name': input("Enter the habit you want to build: "),
        'duration': int(input("Enter the duration in days: ")),  
    })

    builder = SmartHabitBuilder()
    result = builder.run(user_input)
    print("Habit Building Plan:", result)


if __name__ == "__main__":
    main()
