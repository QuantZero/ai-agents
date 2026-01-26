# agent.py

import os
import sys
import json
import logging
from dotenv import load_dotenv
from schemas import GroceryInput, GroceryOutput
from graph import run_grocery_state_machine

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


def main():
    try:
        # Parse input
        if len(sys.argv) != 2:
            logging.error("Usage: python agent.py <input_json_file>")
            sys.exit(1)

        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            input_data = json.load(file)

        # Validate input
        grocery_input = GroceryInput(**input_data)

        # Run the state machine
        result = run_grocery_state_machine(grocery_input)

        # Produce output
        output = GroceryOutput(**result)
        print(output.json())

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
