# graph.py

from langgraph import StateMachine, State
from schemas import TaskInput, TaskOutput
from typing import List

class TaskPrioritizationFlow(StateMachine):
    def __init__(self):
        super().__init__(initial_state='start')

    def start(self, tasks: List[TaskInput]) -> List[TaskOutput]:
        # Sort tasks by priority and due date
        sorted_tasks = sorted(tasks, key=lambda x: (x.priority, x.due_date))
        return [TaskOutput(
            title=task.title,
            description=task.description,
            scheduled_time=task.due_date,
            priority=task.priority
        ) for task in sorted_tasks]

    def prioritize(self, tasks: List[TaskInput]) -> List[TaskOutput]:
        return self.start(tasks)
