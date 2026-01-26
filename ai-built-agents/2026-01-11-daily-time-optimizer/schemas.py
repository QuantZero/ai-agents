from pydantic import BaseModel
from typing import List, Dict

class Task(BaseModel):
    name: str
    duration: int  # Duration in minutes
    importance: int  # Scale from 1 to 10

class ScheduleInput(BaseModel):
    tasks: List[Task]
    available_time: int  # Available time in minutes

class OptimizedScheduleOutput(BaseModel):
    schedule: List[Dict[str, int]]  # List of task names and start times
