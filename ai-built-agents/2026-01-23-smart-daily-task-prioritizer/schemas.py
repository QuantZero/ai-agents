# schemas.py

from pydantic import BaseModel, Field
from typing import List

class TaskInput(BaseModel):
    title: str = Field(..., description="Title of the task")
    description: str = Field(..., description="Description of the task")
    due_date: str = Field(..., description="Due date in YYYY-MM-DD format")
    priority: int = Field(..., ge=1, le=5, description="Priority level (1-5)")

class TaskOutput(BaseModel):
    title: str
    description: str
    scheduled_time: str
    priority: int

class TaskState(BaseModel):
    tasks: List[TaskInput]
    ordered_tasks: List[TaskOutput]
