from pydantic import BaseModel


class TestResponse(BaseModel):
    id: int
    name: str
    category_id: int


class TestPayload(BaseModel):
    name: str
    category_id: int
