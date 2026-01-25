
import os
import sys
from dotenv import load_dotenv
from schemas import TaskInput
from graph import TaskStateMachine
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


def main(task_description: str, estimated_time: int):
    try:
        # Validate input
        task_input = TaskInput(description=task_description, estimated_time=estimated_time)
        
        # Initialize task state machine
        task_machine = TaskStateMachine(task_input)
        task_machine.run()

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        logging.error("Usage: python agent.py <task_description> <estimated_time>")
        sys.exit(1)

    task_description = sys.argv[1]
    try:
        estimated_time = int(sys.argv[2])
    except ValueError:
        logging.error("Estimated time must be an integer.")
        sys.exit(1)

    main(task_description, estimated_time)
