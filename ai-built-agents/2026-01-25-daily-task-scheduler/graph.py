
from langgraph import StateMachine, State
from schemas import TaskInput, TaskState


class TaskStateMachine(StateMachine):
    def __init__(self, task_input: TaskInput):
        initial_state = State(name="Planning", on_enter=self.plan_task)
        super().__init__(initial_state)
        self.task_state = TaskState(current_task=task_input)

    def plan_task(self):
        print(f"Planning task: {self.task_state.current_task.description}")
        self.transition_to(State(name="In Progress", on_enter=self.start_task))

    def start_task(self):
        print(f"Starting task: {self.task_state.current_task.description}")
        # Simulating task completion
        self.transition_to(State(name="Completed", on_enter=self.complete_task))

    def complete_task(self):
        self.task_state.is_completed = True
        print(f"Task '{self.task_state.current_task.description}' completed in {self.task_state.current_task.estimated_time} minutes.")
