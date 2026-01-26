# agent.py

import os
import sys
from dotenv import load_dotenv
from langchain_openai import OpenAIClient
from langgraph import StateMachine
from schemas import ExerciseInput, ExerciseOutput
from graph import exercise_flow
from pydantic import ValidationError

# Load environment variables
load_dotenv()

# Initialize OpenAI client
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("Error: OPENAI_API_KEY is not set.")
    sys.exit(1)

openai_client = OpenAIClient(api_key=API_KEY)


def main(user_input):
    """Main execution logic for the Exercise Companion."""
    try:
        input_data = ExerciseInput.parse_raw(user_input)
    except ValidationError as e:
        print(f"Input validation error: {e}")
        return

    state_machine = StateMachine(flow=exercise_flow, openai_client=openai_client)
    output_data = state_machine.run(initial_input=input_data.dict())

    output = ExerciseOutput.parse_obj(output_data)
    print(output.json(indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py '<user_input_json>'")
        sys.exit(1)

    user_input = sys.argv[1]
    main(user_input)
