from pydantic import BaseModel


class SettingResponse(BaseModel):
    id: int
    category_id: int
    test_amount: int


class SettingPayload(BaseModel):
    category_id: int
    test_amount: int
