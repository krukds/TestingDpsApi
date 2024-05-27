from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from db.models import ResultModel
from db.services.main_services import ResultService
from utils import datetime_now
from .schemes import ResultPayload, ResultResponse

router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


@router.get("")
async def get_all_results() -> list[ResultResponse]:
    results = await ResultService.select()
    if not results:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No results found")

    return results


@router.post("")
async def add_result(
        payload: ResultPayload
) -> ResultResponse:
    result: ResultModel = await ResultService.save(
        ResultModel(
            **payload.model_dump(),
            created_at=datetime_now()
        )
    )
    return ResultResponse(**result.__dict__)


@router.get("/{result_id}")
async def get_result_by_id(
        result_id: int
) -> ResultResponse:
    result: ResultModel = await ResultService.select_one(
        ResultModel.id == result_id
    )
    if not result:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No result with this id found")

    return ResultResponse(**result.__dict__)


# @router.put("/{result_id}")
# async def update_result(
#         result_id: int,
#         payload: ResultPayload
# ) -> ResultResponse:
#     result: ResultModel = await ResultService.select_one(
#         ResultModel.id == result_id
#     )
#     if not result:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No result with this id found")
#
#     for key, value in payload.model_dump().items():
#         setattr(result, key, value)
#
#     updated_result = await ResultService.save(result)
#
#     return ResultResponse(**updated_result.__dict__)


# @router.delete("/{result_id}")
# async def delete_result(
#         result_id: int
# ):
#     result: ResultModel = await ResultService.select_one(
#         ResultModel.id == result_id
#     )
#     if not result:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No result with this id found")
#     await ResultService.delete(id=result_id)
#
#     return {"status": "success"}
