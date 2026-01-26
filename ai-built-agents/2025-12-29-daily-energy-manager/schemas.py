from pydantic import BaseModel

class UserPreferences(BaseModel):
    user_id: str
    wake_time: str  # Expected format "HH:MM"

class EnergyRecommendations(BaseModel):
    work_periods: list[str]
    rest_periods: list[str]
    energizing_activities: list[str]
