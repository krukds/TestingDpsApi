from typing import Optional

from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str


class CategoryPayload(BaseModel):
    name: str