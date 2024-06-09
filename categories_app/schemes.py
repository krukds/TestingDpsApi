from typing import Optional

from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str
    testing_id: int


class CategoryPayload(BaseModel):
    name: str
    testing_id: int
