import os
import sys
from dotenv import load_dotenv
from langchain_openai import OpenAI
from graph import ParentingStateGraph
from schemas import ParentingInput, ParentingOutput


def main():
    # Load environment variables
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("Error: OPENAI_API_KEY is not set.")
        sys.exit(1)

    # Initialize OpenAI client
    openai_client = OpenAI(api_key=openai_api_key)

    # Initialize state machine
    state_graph = ParentingStateGraph(openai_client)

    # Sample input
    user_input = ParentingInput(
        child_name="John",
        age=5,
        preferences={"meal": "vegetarian", "activity": "outdoor"},
        health_info={"allergies": ["peanuts"]}
    )

    # Run the agent
    try:
        output = state_graph.run(user_input)
        print(output.json())
    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
