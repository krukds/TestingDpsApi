from pydantic import BaseModel


class AnswerResponse(BaseModel):
    id: int
    name: str
    test_id: int
    is_correct: bool


class AnswerPayload(BaseModel):
    name: str
    test_id: int
    is_correct: bool
