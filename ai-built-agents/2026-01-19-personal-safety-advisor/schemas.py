from pydantic import BaseModel


class LocationInput(BaseModel):
    location_name: str


class SafetyAdviceOutput(BaseModel):
    advice: str