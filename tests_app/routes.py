from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette.status import HTTP_404_NOT_FOUND

from db.models import TestModel, CategoryModel
from db.services.main_services import TestService, CategoryService
from .schemes import TestPayload, TestResponse

router = APIRouter(
    prefix="/tests",
    tags=["Tests"]
)


@router.get("")
async def get_all_tests(
    category_id: int = None
) -> list[TestResponse]:

    base_query = select(TestModel)

    if category_id is not None:
        category: CategoryModel = await CategoryService.select_one(
            CategoryModel.id == category_id
        )
        if not category:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No category with this id found")

        base_query = base_query.where(TestModel.category_id==category_id)

    tests = await TestService.execute(base_query)
    if not tests:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No tests found")

    return tests


@router.post("")
async def add_test(
        payload: TestPayload
) -> TestResponse:
    test: TestModel = await TestService.save(
        TestModel(
            **payload.model_dump()
        )
    )
    return TestResponse(**test.__dict__)


@router.get("/{test_id}")
async def get_test_by_id(
        test_id: int
) -> TestResponse:
    test: TestModel = await TestService.select_one(
        TestModel.id == test_id
    )
    if not test:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No test with this id found")

    return TestResponse(**test.__dict__)


@router.put("/{test_id}")
async def update_test(
        test_id: int,
        payload: TestPayload
) -> TestResponse:
    test: TestModel = await TestService.select_one(
        TestModel.id == test_id
    )
    if not test:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No test with this id found")

    for key, value in payload.model_dump().items():
        setattr(test, key, value)

    updated_test = await TestService.save(test)

    return TestResponse(**updated_test.__dict__)


@router.delete("/{test_id}")
async def delete_test(
        test_id: int
):
    test: TestModel = await TestService.select_one(
        TestModel.id == test_id
    )
    if not test:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No test with this id found")
    await TestService.delete(id=test_id)

    return {"status": "success"}

