# agent.py

import os
import sys
import openai
from langgraph import LangGraph
from schemas import CheckInInput, CheckInOutput
from prompts import SYSTEM_PROMPT, USER_PROMPT
from dotenv import load_dotenv
from pydantic import ValidationError


def load_environment_variables():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise EnvironmentError("Missing OpenAI API key. Please set OPENAI_API_KEY in your environment.")


def execute_check_in(user_input: str) -> CheckInOutput:
    try:
        # Validate input
        input_data = CheckInInput(text=user_input)

        # Initialize LangGraph
        graph = LangGraph(system_prompt=SYSTEM_PROMPT, user_prompt=USER_PROMPT)
        response = graph.run(input_data.dict(), openai)

        # Validate and return output
        output_data = CheckInOutput.parse_obj(response)
        return output_data
    except ValidationError as e:
        print(f"Validation Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def main():
    load_environment_variables()

    if len(sys.argv) < 2:
        print("Usage: python agent.py '<your_check_in_text>'")
        sys.exit(1)

    user_input = sys.argv[1]
    result = execute_check_in(user_input)
    print(f"AI Response: {result.response}")


if __name__ == "__main__":
    main()
