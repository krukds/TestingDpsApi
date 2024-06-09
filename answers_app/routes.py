from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette.status import HTTP_404_NOT_FOUND

from db.models import AnswerModel
from db.services.main_services import AnswerService
from .schemes import AnswerPayload, AnswerResponse

router = APIRouter(
    prefix="/answers",
    tags=["Answers"]
)


@router.get("")
async def get_all_answers(
    test_id: int = None
) -> list[AnswerResponse]:
    base_query = select(AnswerModel)

    if test_id is not None:
        base_query = base_query.where(AnswerModel.test_id==test_id)

    answers = await AnswerService.execute(base_query)
    if not answers:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No answers found")

    return answers


@router.post("")
async def add_answer(
        payload: AnswerPayload
) -> AnswerResponse:
    answer: AnswerModel = await AnswerService.save(
        AnswerModel(
            **payload.model_dump()
        )
    )
    return AnswerResponse(**answer.__dict__)


@router.get("/{answer_id}")
async def get_answer_by_id(
        answer_id: int
) -> AnswerResponse:
    answer: AnswerModel = await AnswerService.select_one(
        AnswerModel.id == answer_id
    )
    if not answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No answer with this id found")

    return AnswerResponse(**answer.__dict__)


@router.put("/{answer_id}")
async def update_answer(
        answer_id: int,
        payload: AnswerPayload
) -> AnswerResponse:
    answer: AnswerModel = await AnswerService.select_one(
        AnswerModel.id == answer_id
    )
    if not answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No answer with this id found")

    for key, value in payload.model_dump().items():
        setattr(answer, key, value)

    updated_answer = await AnswerService.save(answer)

    return AnswerResponse(**updated_answer.__dict__)


@router.delete("/{answer_id}")
async def delete_answer(
        answer_id: int
):
    answer: AnswerModel = await AnswerService.select_one(
        AnswerModel.id == answer_id
    )
    if not answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No answer with this id found")
    await AnswerService.delete(id=answer_id)

    return {"status": "success"}
