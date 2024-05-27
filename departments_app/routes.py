import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Query
from starlette.status import HTTP_404_NOT_FOUND

from db.models import LocationModel
from db.services.main_services import DepartmentService
from .schemes import DepartmentResponse

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.get("")
async def get_all_departments() -> list[DepartmentResponse]:
    departments = await DepartmentService.select()
    if not departments:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No departments found")

    return departments
