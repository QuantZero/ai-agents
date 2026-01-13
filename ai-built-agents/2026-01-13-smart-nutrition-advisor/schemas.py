from pydantic import BaseModel
from typing import Optional

class UserInput(BaseModel):
    age: int
    weight: float
    height: float
    activity_level: str
    dietary_preferences: Optional[str] = None

class NutritionAdvice(BaseModel):
    advice: str
