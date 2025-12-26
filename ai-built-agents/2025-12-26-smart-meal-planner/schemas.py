# schemas.py

from pydantic import BaseModel
from typing import List, Optional


class MealPlanInput(BaseModel):
    dietary_restrictions: Optional[List[str]] = None
    preferred_cuisine: Optional[str] = None
    number_of_meals: int
    time_constraint: Optional[int] = None  # in minutes


class MealPlanOutput(BaseModel):
    meals: List[str]
    shopping_list: List[str]