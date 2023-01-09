import typing
from fastapi import HTTPException
from pydantic import BaseModel, constr, Field, root_validator
from pydantic.networks import EmailStr
from starlette import status


class RegisterSchema(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    phone: str = Field(..., description="user phone", regex=r"^998\d{9}$")
    last_name: str
    first_name: str
    middle_name: str

    @root_validator
    def check_password_match(cls, values: dict) -> dict:
        password = values.get('password')
        confirm_password = values.pop('confirm_password')
        if password != confirm_password:
            raise HTTPException(detail="The two passwords did not match.",
                                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return values


class RPCErrorSchema(BaseModel):
    error: typing.Any


class RegisterResponseSchema(BaseModel):
    id: str
    email: str
    phone: str
    last_name: str
    first_name: str
    middle_name: str


class LoginUserSchema(BaseModel):
    username: EmailStr
    password: constr(min_length=8)


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str


class RefreshTokenResponseSchema(BaseModel):
    access_token: str


class UsersMeSchema(BaseModel):
    id: str
    email: str
