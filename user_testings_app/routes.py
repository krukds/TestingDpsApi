from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette.status import HTTP_404_NOT_FOUND

from db.models import UserTestingModel
from db.services.main_services import UserTestingService
from .schemes import UserTestingPayload, UserTestingResponse

router = APIRouter(
    prefix="/user-testings",
    tags=["User Testings"]
)


@router.get("")
async def get_all_user_testings(
        user_id: int = None,
        testing_id: int = None
) -> list[UserTestingResponse]:
    base_query = select(UserTestingModel)

    if user_id is not None:
        base_query = base_query.where(UserTestingModel.user_id == user_id)

    if testing_id is not None:
        base_query = base_query.where(UserTestingModel.testing_id == testing_id)

    user_testings = await UserTestingService.execute(base_query)
    if not user_testings:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user testings found")

    return user_testings


@router.post("")
async def add_user_testing(
        payload: UserTestingPayload
) -> UserTestingResponse:
    user_testing: UserTestingModel = await UserTestingService.save(
        UserTestingModel(
            **payload.model_dump()
        )
    )
    return UserTestingResponse(**user_testing.__dict__)


@router.get("/{user_testing_id}")
async def get_user_testing_by_id(
        user_testing_id: int
) -> UserTestingResponse:
    user_testing: UserTestingModel = await UserTestingService.select_one(
        UserTestingModel.id == user_testing_id
    )
    if not user_testing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user testing with this id found")

    return UserTestingResponse(**user_testing.__dict__)


# @router.put("/{user_testing_id}")
# async def update_user_testing(
#         user_testing_id: int,
#         payload: UserTestingPayload
# ) -> UserTestingResponse:
#     user_testing: UserTestingModel = await UserTestingService.select_one(
#         UserTestingModel.id == user_testing_id
#     )
#     if not user_testing:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user testing with this id found")
#
#     for key, value in payload.model_dump().items():
#         setattr(user_testing, key, value)
#
#     updated_user_testing = await UserTestingService.save(user_testing)
#
#     return UserTestingResponse(**updated_user_testing.__dict__)
#
#
@router.delete("/{user_testing_id}")
async def delete_user_testing(
        user_testing_id: int
):
    user_testing: UserTestingModel = await UserTestingService.select_one(
        UserTestingModel.id == user_testing_id
    )
    if not user_testing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No user testing with this id found")
    await UserTestingService.delete(id=user_testing_id)

    return {"status": "success"}
