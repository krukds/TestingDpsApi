from pydantic import BaseModel


class ResultResponse(BaseModel):
    id: int
    user_id: int
    testing_id: int
    rating: int
    created_at: str


class ResultPayload(BaseModel):
    user_id: int
    testing_id: int
    rating: int
