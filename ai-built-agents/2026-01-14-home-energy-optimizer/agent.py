import os
import sys
import logging
from dotenv import load_dotenv
from home_assistant_api import HomeAssistantAPI
from langgraph import StateMachine
from openai import OpenAIManager
from schemas import EnergyOptimizationInput, OptimizationResult
from graph import EnergyOptimizationGraph

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Main execution logic
def main():
    try:
        # Initialize API clients and state machine
        home_assistant_api = HomeAssistantAPI(os.getenv('HOME_ASSISTANT_API_KEY'))
        openai_manager = OpenAIManager(os.getenv('OPENAI_API_KEY'))
        state_machine = StateMachine(EnergyOptimizationGraph())

        # Collect input data
        user_input = EnergyOptimizationInput(
            current_temperature=home_assistant_api.get_current_temperature(),
            energy_prices=home_assistant_api.get_energy_prices()
        )

        # Run state machine
        result = state_machine.run(user_input)

        # Output the results
        if isinstance(result, OptimizationResult):
            logger.info(f"Recommended actions: {result.actions}")
            logger.info(f"Expected savings: {result.savings}")
        else:
            logger.error("Failed to optimize energy usage.")

    except Exception as e:
        logger.exception("An error occurred during execution.")
        sys.exit(1)

if __name__ == "__main__":
    main()
