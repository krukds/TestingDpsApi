from typing import Optional

from pydantic import BaseModel


class TestingResponse(BaseModel):
    id: int
    name: str
    time: int


class TestingPayload(BaseModel):
    name: str
    time: int
