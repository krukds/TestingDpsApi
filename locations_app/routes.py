import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Query
from starlette.status import HTTP_404_NOT_FOUND

from db.models import LocationModel
from db.services.main_services import LocationService
from .schemes import LocationResponse

router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)


@router.get("")
async def get_all_locations() -> list[LocationResponse]:
    locations = await LocationService.select()
    if not locations:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No locations found")

    return locations
