from pydantic import BaseModel, Field
from typing import Dict

class ExpenseInput(BaseModel):
    income: float = Field(..., description="Monthly income amount")
    fixed_expenses: Dict[str, float] = Field(..., description="Dictionary of fixed expenses like rent, utilities")
    variable_expenses: Dict[str, float] = Field(..., description="Dictionary of variable expenses like groceries, entertainment")
    savings_goal: float = Field(..., description="Monthly savings goal")

class ExpenseOutput(BaseModel):
    total_expenses: float = Field(..., description="Total amount of expenses calculated")
    remaining_budget: float = Field(..., description="Remaining budget after expenses and savings goal")
    advice: str = Field(..., description="Financial advice to optimize spending")
