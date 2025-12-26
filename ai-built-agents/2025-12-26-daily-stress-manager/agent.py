import os
import sys
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from schemas import StressInput, StressOutput
from graph import stress_management_flow

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY is not set.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY


def get_stress_management_advice(input_data: StressInput) -> StressOutput:
    """
    Uses OpenAI API to provide stress management advice based on user input.
    """
    try:
        # Create a prompt for the LLM
        prompt = (
            f"User is feeling stressed because: {input_data.stressors} \n"
            f"They rate their stress level at: {input_data.stress_level}/10 \n"
            f"Provide them with practical advice to manage their stress."
        )

        # Call OpenAI API to get a response
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        advice = response.choices[0].text.strip()
        return StressOutput(advice=advice)

    except Exception as e:
        print(f"Error during API call: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Usage: python agent.py <stressors> <stress_level>")
        sys.exit(1)

    try:
        input_data = StressInput(stressors=sys.argv[1], stress_level=int(sys.argv[2]))
        output_data = get_stress_management_advice(input_data)
        print(f"Stress Management Advice: {output_data.advice}")

    except ValidationError as e:
        print(f"Input validation error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()