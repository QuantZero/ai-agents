# agent.py

import os
import sys
import logging
from dotenv import load_dotenv
from langgraph import LangGraph
from openai import OpenAI
from schemas import SleepInput, SleepOutput

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key=openai_api_key)

# Define the main execution logic
def main():
    try:
        # Parse input
        user_input = parse_input()

        # Validate input
        input_data = SleepInput(**user_input)

        # Initialize the sleep optimizer state machine
        graph = LangGraph(input_data)

        # Execute the state machine
        result = graph.run()

        # Validate and output results
        output_data = SleepOutput(**result)
        print(output_data.json())

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)


def parse_input():
    # Dummy function to simulate input parsing
    # Replace with actual CLI parsing logic or input method
    return {
        "sleep_duration": 6.5,
        "sleep_quality": "poor",
        "stress_level": "high",
        "caffeine_intake": "moderate",
        "exercise_frequency": "low"
    }

if __name__ == "__main__":
    main()
