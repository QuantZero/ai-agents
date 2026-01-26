# schemas.py

from pydantic import BaseModel, validator


class SecurityInput(BaseModel):
    address: str

    @validator('address')
    def address_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Address must not be empty')
        return v
