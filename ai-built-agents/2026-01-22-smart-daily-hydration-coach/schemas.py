from pydantic import BaseModel, Field

class HydrationInput(BaseModel):
    weight_kg: float = Field(..., gt=0, description="The user's weight in kilograms")
    activity_level: float = Field(..., ge=0, le=1, description="The user's activity level where 0 is sedentary and 1 is highly active")

class HydrationOutput(BaseModel):
    recommended_water_intake_liters: float = Field(..., description="Recommended daily water intake in liters")