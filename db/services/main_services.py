from db.base import async_session_maker
from db.models import (UserModel, SessionModel, TestingModel, TestModel, CategoryModel, SettingModel, AnswerModel,
                       ResultModel, UserTestAnswerModel, UserTestingModel, LocationModel, DepartmentModel)
from db.services.base_service import BaseService


class UserService(BaseService[UserModel]):
    model = UserModel
    session_maker = async_session_maker


class SessionService(BaseService[SessionModel]):
    model = SessionModel
    session_maker = async_session_maker


class TestingService(BaseService[TestingModel]):
    model = TestingModel
    session_maker = async_session_maker


class TestService(BaseService[TestModel]):
    model = TestModel
    session_maker = async_session_maker


class CategoryService(BaseService[CategoryModel]):
    model = CategoryModel
    session_maker = async_session_maker


class SettingService(BaseService[SettingModel]):
    model = SettingModel
    session_maker = async_session_maker


class AnswerService(BaseService[AnswerModel]):
    model = AnswerModel
    session_maker = async_session_maker


class ResultService(BaseService[ResultModel]):
    model = ResultModel
    session_maker = async_session_maker


class UserTestAnswerService(BaseService[UserTestAnswerModel]):
    model = UserTestAnswerModel
    session_maker = async_session_maker


class UserTestingService(BaseService[UserTestingModel]):
    model = UserTestingModel
    session_maker = async_session_maker



class LocationService(BaseService[LocationModel]):
    model = LocationModel
    session_maker = async_session_maker


class DepartmentService(BaseService[DepartmentModel]):
    model = DepartmentModel
    session_maker = async_session_maker





