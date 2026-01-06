# schemas.py

from pydantic import BaseModel, validator

class CommuteRequest(BaseModel):
    start_location: str
    end_location: str
    
    @validator('start_location', 'end_location')
    def locations_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Location must not be empty')
        return v

class CommuteResponse(BaseModel):
    estimated_time: str
    optimal_route: str
    traffic_conditions: str
