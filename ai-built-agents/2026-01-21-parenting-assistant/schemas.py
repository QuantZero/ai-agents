from pydantic import BaseModel
from typing import Dict, List


class ParentingInput(BaseModel):
    child_name: str
    age: int
    preferences: Dict[str, str]
    health_info: Dict[str, List[str]]


class ParentingOutput(BaseModel):
    meal_plan: str
    activity_suggestion: str
    health_advice: str
