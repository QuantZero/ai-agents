from pydantic import BaseModel, validator
from typing import List, Optional
import json

class JobApplication(BaseModel):
    company_name: str
    position: str
    application_date: str
    status: str = "Pending"
    follow_up_date: Optional[str] = None

    @validator('application_date', 'follow_up_date', pre=True, always=True)
    def validate_dates(cls, v):
        # Simple date validation can be added here
        return v

    @staticmethod
    def load_from_file(file_path: str) -> List['JobApplication']:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return [JobApplication(**item) for item in data]
