from pydantic import BaseModel, Field

class FileOrganizationInput(BaseModel):
    directory: str = Field(..., description="Directory path for file organization.")

class EmailOrganizationInput(BaseModel):
    email_account: str = Field(..., description="Email account to organize.")
    email_password: str = Field(..., description="Password for the email account.")
