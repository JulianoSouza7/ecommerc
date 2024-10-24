from pydantic import BaseModel, EmailStr


class Create_user(BaseModel):
    username: str
    password: str
    email: EmailStr