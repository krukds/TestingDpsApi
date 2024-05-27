from typing import Optional

from pydantic import BaseModel


class LocationResponse(BaseModel):
    id: int
    name: str
