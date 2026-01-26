# agent.py

import os
import sys
import logging
from dotenv import load_dotenv
from langchain_openai import OpenAIClient
from pydantic import ValidationError
from schemas import SecurityInput
from tools import get_crime_data, evaluate_security

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI Client
openai_client = OpenAIClient(api_key=os.getenv('OPENAI_API_KEY'))


def main(address: str):
    try:
        # Validate input
        security_input = SecurityInput(address=address)

        # Fetch crime data
        crime_data = get_crime_data(security_input.address)

        # Evaluate security
        security_advice = evaluate_security(crime_data)

        print("Security Advice:")
        print(security_advice)

    except ValidationError as e:
        logger.error(f"Validation error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python agent.py <address>")
    else:
        main(sys.argv[1])
