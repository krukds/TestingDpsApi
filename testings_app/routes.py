from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from db.models import TestingModel
from db.services.main_services import TestingService
from .schemes import TestingPayload, TestingResponse

router = APIRouter(
    prefix="/testings",
    tags=["Testings"]
)


@router.get("")
async def get_all_testings() -> list[TestingResponse]:
    testings = await TestingService.select()
    if not testings:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No testings found")

    return testings


@router.post("")
async def add_testing(
        payload: TestingPayload
) -> TestingResponse:
    testing: TestingModel = await TestingService.save(
        TestingModel(
            **payload.model_dump()
        )
    )
    return TestingResponse(**testing.__dict__)


@router.get("/{testing_id}")
async def get_testing_by_id(
        testing_id: int
) -> TestingResponse:
    testing: TestingModel = await TestingService.select_one(
        TestingModel.id == testing_id
    )
    if not testing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No testing with this id found")

    return TestingResponse(**testing.__dict__)


@router.put("/{testing_id}")
async def update_testing(
        testing_id: int,
        payload: TestingPayload
) -> TestingResponse:
    testing: TestingModel = await TestingService.select_one(
        TestingModel.id == testing_id
    )
    if not testing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No testing with this id found")

    for key, value in payload.model_dump().items():
        setattr(testing, key, value)

    updated_testing = await TestingService.save(testing)

    return TestingResponse(**updated_testing.__dict__)


@router.delete("/{testing_id}")
async def delete_testing(
        testing_id: int
):
    testing: TestingModel = await TestingService.select_one(
        TestingModel.id == testing_id
    )
    if not testing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No testing with this id found")
    await TestingService.delete(id=testing_id)

    return {"status": "success"}

