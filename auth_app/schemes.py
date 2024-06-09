from typing import Optional

from pydantic import BaseModel


class TokenPayload(BaseModel):
    user_id: int
    expires_at: int


class LoginPayload(BaseModel):
    username: str
    password: str


class SignupPayload(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    phone: str
    location_id: int
    department_id: int


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: Optional[str]


class UserResponse(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    phone: str
    location_id: int
    department_id: int


class UserDetailResponse(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    phone: str
    location: str
    department: str


class UserPayload(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    phone: str
    location_id: int
    department_id: int
