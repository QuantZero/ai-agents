from pydantic import BaseModel
from datetime import datetime

class MedicationInput(BaseModel):
    name: str
    time: str  # Expected format 'HH:MM'
    phone_number: str

    def is_due(self) -> bool:
        current_time = datetime.now().strftime('%H:%M')
        return self.time == current_time

class ReminderOutput(BaseModel):
    medication_name: str
    time: str
