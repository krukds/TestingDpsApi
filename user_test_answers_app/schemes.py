from pydantic import BaseModel


class UserTestAnswerResponse(BaseModel):
    id: int
    user_id: int
    answer_id: int
    test_id: int


class UserTestAnswerPayload(BaseModel):
    user_id: int
    answer_id: int
    test_id: int
