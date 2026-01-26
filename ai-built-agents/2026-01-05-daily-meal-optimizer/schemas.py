from pydantic import BaseModel, Field

class MealPlanInput(BaseModel):
    dietary_preferences: str = Field(..., description="User's dietary preferences, e.g., vegetarian, vegan, etc.")
    budget: str = Field(..., description="User's budget for meal planning, e.g., $50 per week")

class MealPlanOutput(BaseModel):
    meals: list[str] = Field(..., description="List of meals planned for the user")

    @classmethod
    def from_response(cls, response):
        # Assuming the response is a dictionary with key 'meals'
        return cls(meals=response.get('meals', []))