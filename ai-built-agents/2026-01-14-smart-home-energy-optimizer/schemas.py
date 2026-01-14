from pydantic import BaseModel
from typing import List, Optional

class EnergyOptimizationInput(BaseModel):
    current_temperature: float
    energy_prices: List[float]

class OptimizationResult(BaseModel):
    actions: List[str]
    savings: Optional[float]
