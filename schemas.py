from pydantic import BaseModel


class RegisterSchema(BaseModel):
    username: str
    password: str
    email: str


class RegisterResponseSchema(BaseModel):
    id: int
    username: str
    email: str
