# schemas.py

from pydantic import BaseModel, Field

class SleepInput(BaseModel):
    sleep_duration: float = Field(..., description="Duration of sleep in hours")
    sleep_quality: str = Field(..., description="Quality of sleep (e.g., good, average, poor)")
    stress_level: str = Field(..., description="Stress level (e.g., low, moderate, high)")
    caffeine_intake: str = Field(..., description="Caffeine intake level (e.g., low, moderate, high)")
    exercise_frequency: str = Field(..., description="Frequency of exercise (e.g., low, moderate, high)")

class SleepOutput(BaseModel):
    recommendations: str = Field(..., description="Recommended actions to improve sleep")
