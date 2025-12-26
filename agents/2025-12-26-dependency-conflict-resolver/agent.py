# agent.py

import os
import sys
import logging
from dotenv import load_dotenv
from dependency_checker import check_for_conflicts
from schemas import DependencyConflictInput, DependencyConflictOutput
from langgraph import DependencyConflictResolverFlow

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        # Parse command line arguments
        if len(sys.argv) != 2:
            raise ValueError("Usage: python agent.py <path_to_requirements_file>")

        requirements_file = sys.argv[1]

        # Validate input
        input_data = DependencyConflictInput(requirements_file=requirements_file)

        # Check for dependency conflicts
        conflicts = check_for_conflicts(input_data.requirements_file)

        # Resolve conflicts using the state machine
        resolver_flow = DependencyConflictResolverFlow()
        resolved_output = resolver_flow.resolve(conflicts)

        # Return output
        output_data = DependencyConflictOutput(conflicts=conflicts, resolution=resolved_output)
        logger.info("Dependency conflicts resolved:")
        logger.info(output_data.json(indent=2))

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
