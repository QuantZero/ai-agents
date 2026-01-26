import os
import sys
import openai
from dotenv import load_dotenv
from langgraph import StateMachine
from schemas import CareerInput
from graph import career_state_machine

# Load environment variables
load_dotenv()

# OpenAI API setup
openai.api_key = os.getenv('OPENAI_API_KEY')


def main():
    try:
        # Parse input
        input_data = CareerInput.parse_raw(sys.stdin.read())

        # Initialize the state machine
        sm = StateMachine(career_state_machine)

        # Run the agent logic
        result = sm.run(input_data)

        # Output the result
        print(result.json())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
