from pydantic import BaseModel, EmailStr
from typing import List

class ScheduleRequest(BaseModel):
    user_email: EmailStr
    friend_emails: List[EmailStr]
    preferred_days: List[str]  # Example: ['Saturday', 'Sunday']
    time_slots: List[str]  # Example: ['18:00-20:00', '20:00-22:00']

class EventSuggestion(BaseModel):
    day: str
    time_slot: str
    participants: List[EmailStr]

class SchedulerState(BaseModel):
    current_step: str
    suggestions: List[EventSuggestion] = []
