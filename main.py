from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, Depends

import auth_app, locations_app, categories_app, departments_app, testings_app, tests_app, answers_app,\
    settings_app, results_app, user_test_answers_app, user_testings_app


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


app = FastAPI(
    title="Testing Dps Api",
    lifespan=lifespan
)

secured_router = APIRouter(
    prefix="/api",
    dependencies=[Depends(auth_app.get_current_active_user)]
)

api_router = APIRouter(
    prefix="/api",
)

api_router.include_router(auth_app.router)
api_router.include_router(locations_app.router)
api_router.include_router(categories_app.router)
api_router.include_router(departments_app.router)
api_router.include_router(testings_app.router)
api_router.include_router(tests_app.router)
api_router.include_router(answers_app.router)
api_router.include_router(settings_app.router)
api_router.include_router(results_app.router)
api_router.include_router(user_test_answers_app.router)
api_router.include_router(user_testings_app.router)

# secured_router.include_router(event_tickets_app.router)

app.include_router(api_router)
# app.include_router(secured_router)
# app.include_router(frontend_app.router)

