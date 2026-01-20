from pydantic import BaseModel, Field

class EnergyUsageInput(BaseModel):
    area_size: float = Field(..., description="Size of the home in square feet")
    num_occupants: int = Field(..., description="Number of occupants in the home")
    energy_rate: float = Field(..., description="Energy rate per kWh")