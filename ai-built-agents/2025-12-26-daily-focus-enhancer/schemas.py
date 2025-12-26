from pydantic import BaseModel


class FocusInput(BaseModel):
    user_input: str


class FocusOutput(BaseModel):
    focus_advice: str
