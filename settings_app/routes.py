from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from db.models import SettingModel
from db.services.main_services import SettingService
from .schemes import SettingPayload, SettingResponse

router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)


@router.get("")
async def get_all_settings() -> list[SettingResponse]:
    settings = await SettingService.select()
    if not settings:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No settings found")

    return settings


@router.post("")
async def add_setting(
        payload: SettingPayload
) -> SettingResponse:
    setting: SettingModel = await SettingService.save(
        SettingModel(
            **payload.model_dump()
        )
    )
    return SettingResponse(**setting.__dict__)


@router.get("/{setting_id}")
async def get_setting_by_id(
        setting_id: int
) -> SettingResponse:
    setting: SettingModel = await SettingService.select_one(
        SettingModel.id == setting_id
    )
    if not setting:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No setting with this id found")

    return SettingResponse(**setting.__dict__)


@router.put("/{setting_id}")
async def update_setting(
        setting_id: int,
        payload: SettingPayload
) -> SettingResponse:
    setting: SettingModel = await SettingService.select_one(
        SettingModel.id == setting_id
    )
    if not setting:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No setting with this id found")

    for key, value in payload.model_dump().items():
        setattr(setting, key, value)

    updated_setting = await SettingService.save(setting)

    return SettingResponse(**updated_setting.__dict__)


@router.delete("/{setting_id}")
async def delete_setting(
        setting_id: int
):
    setting: SettingModel = await SettingService.select_one(
        SettingModel.id == setting_id
    )
    if not setting:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No setting with this id found")
    await SettingService.delete(id=setting_id)

    return {"status": "success"}
