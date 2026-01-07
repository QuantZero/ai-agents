from pydantic import BaseModel

class SleepInput(BaseModel):
    sleep_duration: float  # hours
    stress_level: int  # 1 to 10 scale
    environment_noise_level: int  # 1 to 10 scale

class SleepOutput(BaseModel):
    suggestions: str  # Suggestions for improving sleep quality
