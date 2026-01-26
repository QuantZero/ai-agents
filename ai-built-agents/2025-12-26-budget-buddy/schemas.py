from pydantic import BaseModel, Field
from typing import Dict

class BudgetInput(BaseModel):
    income: float = Field(..., description="Total monthly income")
    expenses: Dict[str, float] = Field(..., description="Dictionary of expense categories and amounts")

class BudgetOutput(BaseModel):
    recommendation: str = Field(..., description="Budget recommendation based on input data")