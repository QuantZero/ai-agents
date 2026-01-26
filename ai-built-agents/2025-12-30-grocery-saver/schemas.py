# schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional


class GroceryInput(BaseModel):
    budget: float = Field(..., description="Monthly grocery budget in USD")
    dietary_preferences: Optional[List[str]] = Field(default=None, description="List of dietary preferences or restrictions")
    household_size: int = Field(..., description="Number of people in the household")
    inventory: List[str] = Field(..., description="Current inventory of groceries")


class GroceryOutput(BaseModel):
    suggested_shopping_list: List[str] = Field(..., description="Optimized shopping list within budget")
    estimated_cost: float = Field(..., description="Estimated total cost of the shopping list")
    waste_reduction_tips: List[str] = Field(..., description="Tips to reduce food waste")
