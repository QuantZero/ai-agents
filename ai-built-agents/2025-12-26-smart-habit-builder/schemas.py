# schemas.py

from pydantic import BaseModel, Field, validator

class UserInput(BaseModel):
    habit_name: str = Field(..., description="Name of the habit to build")
    duration: int = Field(..., description="Duration in days to establish the habit")

    @validator('duration')
    def duration_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Duration must be a positive integer')
        return value

class HabitState(BaseModel):
    current_step: int = Field(0, description="Current step in the habit building process")
    habit_name: str = Field(..., description="Name of the habit being established")
    total_days: int = Field(..., description="Total days planned for the habit")
