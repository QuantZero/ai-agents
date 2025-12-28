# schemas.py

from pydantic import BaseModel, Field
from typing import Optional, List


class ExerciseInput(BaseModel):
    user_id: str
    fitness_level: str = Field(..., description="User's current fitness level")
    goals: List[str] = Field(..., description="User's fitness goals")
    preferences: Optional[List[str]] = Field(None, description="User's exercise preferences")


class ExerciseOutput(BaseModel):
    personalized_plan: str
    motivation_tips: Optional[str]


class ExerciseState(BaseModel):
    step: str
    data: dict
