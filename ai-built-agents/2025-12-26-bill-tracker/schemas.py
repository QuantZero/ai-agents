# schemas.py

from pydantic import BaseModel, EmailStr, conlist
from datetime import date

class Bill(BaseModel):
    name: str
    amount: float
    due_date: date

class UserSettings(BaseModel):
    user_email: EmailStr
    bills: conlist(Bill, min_items=1)
    reminder_days: int
