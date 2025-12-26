from pydantic import BaseModel, Field

class StressInput(BaseModel):
    stressors: str = Field(..., description="Description of stressors causing stress.")
    stress_level: int = Field(..., ge=0, le=10, description="Stress level on a scale from 0 to 10.")


class StressOutput(BaseModel):
    advice: str = Field(..., description="Advice for managing stress.")