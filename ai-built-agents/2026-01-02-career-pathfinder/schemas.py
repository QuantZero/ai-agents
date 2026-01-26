from pydantic import BaseModel, Field
from typing import List, Optional


class CareerInput(BaseModel):
    name: str = Field(..., description="Name of the individual")
    skills: List[str] = Field(..., description="List of skills the individual possesses")
    interests: List[str] = Field(..., description="List of interests")
    current_job: Optional[str] = Field(None, description="Current job title if applicable")


class CareerRecommendation(BaseModel):
    recommended_careers: List[str] = Field(..., description="List of recommended career paths")
    rationale: str = Field(..., description="Explanation of why these careers were recommended")
