import os
import sys
from dotenv import load_dotenv
from langgraph import Graph, Node
from openai import OpenAI
from pydantic import BaseModel, ValidationError
from schemas import SleepInput, SleepOutput
from graph import sleep_quality_graph

load_dotenv()

class SmartSleepQualityEnhancer:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.graph = sleep_quality_graph

    def enhance_sleep(self, user_input: SleepInput) -> SleepOutput:
        try:
            # Validate input
            validated_input = SleepInput(**user_input.dict())
            # Process through graph
            result = self.graph.run(self.client, validated_input)
            # Validate and return output
            return SleepOutput(**result)
        except ValidationError as e:
            print(f"Validation error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if 'OPENAI_API_KEY' not in os.environ:
        print("Error: The environment variable 'OPENAI_API_KEY' is not set.")
        sys.exit(1)

    api_key = os.getenv('OPENAI_API_KEY')
    enhancer = SmartSleepQualityEnhancer(api_key)

    # Example CLI input
    user_input = SleepInput(sleep_duration=6, stress_level=8, environment_noise_level=7)
    result = enhancer.enhance_sleep(user_input)
    print("Suggested improvements:", result.suggestions)
