
import os
import sys
import calendar
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from typing import List
from langgraph import StateMachine
from langchain_openai import OpenAI

# Load environment variables
load_dotenv()

# Define Pydantic models
class MaintenanceTask(BaseModel):
    name: str
    frequency: int  # in months
    last_completed: datetime

class SchedulerInput(BaseModel):
    tasks: List[MaintenanceTask]

# Define the state machine using LangGraph
class MaintenanceSchedulerStateMachine(StateMachine):
    def __init__(self):
        super().__init__(self.initial_state)

    def initial_state(self, input_data: SchedulerInput):
        due_tasks = []
        current_month = datetime.now().month
        for task in input_data.tasks:
            months_since_last = (current_month - task.last_completed.month) % 12
            if months_since_last >= task.frequency:
                due_tasks.append(task.name)
        return self.final_state(due_tasks)

    def final_state(self, due_tasks: List[str]):
        if due_tasks:
            return f"Tasks due for maintenance: {', '.join(due_tasks)}"
        else:
            return "All tasks are up to date."

# Main CLI interface
if __name__ == "__main__":
    try:
        # Example data, this could be loaded from a file or user input
        example_data = [
            {"name": "Check Smoke Detectors", "frequency": 6, "last_completed": datetime(2023, 4, 1)},
            {"name": "Clean Gutters", "frequency": 3, "last_completed": datetime(2023, 7, 1)},
            {"name": "Service HVAC", "frequency": 12, "last_completed": datetime(2023, 1, 1)}
        ]

        tasks = [MaintenanceTask(**task) for task in example_data]
        input_data = SchedulerInput(tasks=tasks)

        scheduler = MaintenanceSchedulerStateMachine()
        result = scheduler.run(input_data)

        print(result)

    except ValidationError as e:
        print("Input validation error:", e)
    except Exception as e:
        print("An error occurred:", e)
