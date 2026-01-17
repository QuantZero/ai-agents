# schemas.py

from pydantic import BaseModel, Field


class CheckInInput(BaseModel):
    text: str = Field(..., description="Input text for the mental health check-in")


class CheckInOutput(BaseModel):
    response: str = Field(..., description="AI-generated response to the check-in")
