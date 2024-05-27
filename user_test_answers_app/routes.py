from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from db.models import UserTestAnswerModel
from db.services.main_services import UserTestAnswerService
from .schemes import UserTestAnswerPayload, UserTestAnswerResponse

router = APIRouter(
    prefix="/user-test-answers",
    tags=["User Test Answers"]
)


@router.get("")
async def get_all_user_test_answers() -> list[UserTestAnswerResponse]:
    user_test_answers = await UserTestAnswerService.select()
    if not user_test_answers:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user test answers found")

    return user_test_answers


@router.post("")
async def add_user_test_answer(
        payload: UserTestAnswerPayload
) -> UserTestAnswerResponse:
    user_test_answer: UserTestAnswerModel = await UserTestAnswerService.save(
        UserTestAnswerModel(
            **payload.model_dump()
        )
    )
    return UserTestAnswerResponse(**user_test_answer.__dict__)


@router.get("/{user_test_answer_id}")
async def get_user_test_answer_by_id(
        user_test_answer_id: int
) -> UserTestAnswerResponse:
    user_test_answer: UserTestAnswerModel = await UserTestAnswerService.select_one(
        UserTestAnswerModel.id == user_test_answer_id
    )
    if not user_test_answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user test answer with this id found")

    return UserTestAnswerResponse(**user_test_answer.__dict__)


# @router.put("/{user_test_answer_id}")
# async def update_user_test_answer(
#         user_test_answer_id: int,
#         payload: UserTestAnswerPayload
# ) -> UserTestAnswerResponse:
#     user_test_answer: UserTestAnswerModel = await UserTestAnswerService.select_one(
#         UserTestAnswerModel.id == user_test_answer_id
#     )
#     if not user_test_answer:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user test answer with this id found")
#
#     for key, value in payload.model_dump().items():
#         setattr(user_test_answer, key, value)
#
#     updated_user_test_answer = await UserTestAnswerService.save(user_test_answer)
#
#     return UserTestAnswerResponse(**updated_user_test_answer.__dict__)
#
#
# @router.delete("/{user_test_answer_id}")
# async def delete_user_test_answer(
#         user_test_answer_id: int
# ):
#     user_test_answer: UserTestAnswerModel = await UserTestAnswerService.select_one(
#         UserTestAnswerModel.id == user_test_answer_id
#     )
#     if not user_test_answer:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user test answer with this id found")
#     await UserTestAnswerService.delete(id=user_test_answer_id)
#
#     return {"status": "success"}
