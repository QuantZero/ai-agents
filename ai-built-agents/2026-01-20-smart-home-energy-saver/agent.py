import os
import sys
import logging
from dotenv import load_dotenv
from langgraph import StateMachine
from openai import OpenAI
from schemas import EnergyUsageInput
from graph import EnergySaverFlow

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Main execution logic
def main():
    try:
        # Initialize OpenAI client
        openai_api_key = os.getenv('OPENAI_API_KEY')
        openai_client = OpenAI(api_key=openai_api_key)

        # Initialize the state machine
        energy_saver_flow = EnergySaverFlow(openai_client)

        # Collect user input
        user_input = collect_user_input()
        energy_usage_input = EnergyUsageInput(**user_input)

        # Execute the state machine
        result = energy_saver_flow.run(energy_usage_input)

        # Display results
        print("Suggested Energy Saving Tips:")
        print(result)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


def collect_user_input():
    """Collect user input from the command line."""
    print("Welcome to the Smart Home Energy Saver!")
    area_size = input("Enter the size of your home in square feet: ")
    num_occupants = input("Enter the number of occupants: ")
    energy_rate = input("Enter your energy rate per kWh: ")
    return {
        "area_size": area_size,
        "num_occupants": num_occupants,
        "energy_rate": energy_rate
    }


if __name__ == '__main__':
    main()