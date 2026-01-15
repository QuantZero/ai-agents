# schemas.py

from pydantic import BaseModel, Field

class DisasterPreparednessInput(BaseModel):
    address: str = Field(..., description="The address to check for disaster preparedness")
    latitude: float = Field(None, description="Latitude of the location")
    longitude: float = Field(None, description="Longitude of the location")

class DisasterPreparednessOutput(BaseModel):
    guide: str = Field(..., description="Preparedness guide for the location")