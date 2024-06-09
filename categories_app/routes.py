import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Query
from starlette.status import HTTP_404_NOT_FOUND

from db.models import LocationModel, CategoryModel, TestingModel
from db.services.main_services import CategoryService, TestingService
from .schemes import CategoryResponse, CategoryPayload

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("")
async def get_all_categories(
        testing_id: int = None
) -> list[CategoryResponse]:

    base_query = select(CategoryModel)
    if testing_id is not None:
        testing: TestingModel = await TestingService.select_one(
            TestingModel.id == testing_id
        )
        if not testing:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No testing with this id found")

        base_query = base_query.where(CategoryModel.testing_id == testing_id)

    categories = await CategoryService.execute(base_query)

    if not categories:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No categories found")

    return categories


@router.post("")
async def add_category(
        payload: CategoryPayload
) -> CategoryResponse:
    category: CategoryModel = await CategoryService.save(
        CategoryModel(**payload.model_dump())
    )

    return CategoryResponse(**category.__dict__)


@router.get("/{category_id}")
async def get_category_by_id(
        category_id: int
) -> CategoryResponse:
    category: CategoryModel = await CategoryService.select_one(
        CategoryModel.id == category_id
    )
    if not category:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No category with this id found")

    return CategoryResponse(**category.__dict__)


@router.put("/{category_id}")
async def update_category(
        category_id: int,
        payload: CategoryPayload
) -> CategoryResponse:
    category: CategoryModel = await CategoryService.select_one(
        CategoryModel.id == category_id
    )
    if not category:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No category with this id found")

    for key, value in payload.model_dump().items():
        setattr(category, key, value)

    updated_category = await CategoryService.save(category)

    return CategoryResponse(**updated_category.__dict__)


@router.delete("/{category_id}")
async def delete_category(
        category_id: int
):
    category: CategoryModel = await CategoryService.select_one(
        CategoryModel.id == category_id
    )
    if not category:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No category with this id found")
    await CategoryService.delete(id=category_id)

    return {"status": "success"}

