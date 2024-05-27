from pydantic import BaseModel


class UserTestingResponse(BaseModel):
    id: int
    user_id: int
    testing_id: int


class UserTestingPayload(BaseModel):
    user_id: int
    testing_id: int
