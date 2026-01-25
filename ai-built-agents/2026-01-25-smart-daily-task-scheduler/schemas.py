
from pydantic import BaseModel, Field


class TaskInput(BaseModel):
    description: str = Field(..., title="Task Description", description="A brief description of the task.")
    estimated_time: int = Field(..., gt=0, title="Estimated Time", description="Estimated time to complete the task in minutes.")


class TaskState(BaseModel):
    current_task: TaskInput
    is_completed: bool = False
