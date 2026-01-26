# agent.py

import os
import sys
from dotenv import load_dotenv
from pydantic import ValidationError
from schemas import TaskInput, TaskOutput
from graph import TaskPrioritizationFlow

load_dotenv()

class TaskPrioritizerAgent:
    def __init__(self):
        self.flow = TaskPrioritizationFlow()

    def prioritize_tasks(self, tasks):
        try:
            task_inputs = [TaskInput(**task) for task in tasks]
            prioritized_tasks = self.flow.prioritize(task_inputs)
            return [task.dict() for task in prioritized_tasks]
        except ValidationError as e:
            print("Validation Error: ", e)
            sys.exit(1)
        except Exception as e:
            print("An unexpected error occurred: ", e)
            sys.exit(1)

if __name__ == "__main__":
    import json

    if len(sys.argv) != 2:
        print("Usage: python agent.py <tasks.json>")
        sys.exit(1)

    tasks_file = sys.argv[1]
    try:
        with open(tasks_file, 'r') as file:
            tasks = json.load(file)
            agent = TaskPrioritizerAgent()
            prioritized_tasks = agent.prioritize_tasks(tasks)
            print(json.dumps(prioritized_tasks, indent=2))
    except FileNotFoundError:
        print(f"File {tasks_file} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        sys.exit(1)
