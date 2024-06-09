from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, CheckConstraint, Boolean, Date, \
    UniqueConstraint, Time, Text
from sqlalchemy.orm import relationship, Mapped

from db.base import Base

metadata = Base.metadata


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(255))
    location_id = Column(Integer, ForeignKey('location.id'))
    department_id = Column(Integer, ForeignKey('department.id'))

    location = relationship("LocationModel", back_populates="users")
    department = relationship("DepartmentModel", back_populates="users")

    def __repr__(self) -> str:
        return (
            f'UserModel(id={self.id}, name={self.email})'
        )


class SessionModel(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    access_token = Column(String(255), nullable=True)
    expires_at = Column(DateTime)

    def __repr__(self) -> str:
        return (
            f'SessionModel(id={self.id}, user_id={self.user_id})'
        )


class LocationModel(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    users = relationship("UserModel", back_populates="location")


class DepartmentModel(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    users = relationship("UserModel", back_populates="department")


class TestingModel(Base):
    __tablename__ = 'testing'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    time = Column(Integer, nullable=False)


class TestModel(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)


class CategoryModel(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    testing_id = Column(Integer, ForeignKey('testing.id'), nullable=False)


class SettingModel(Base):
    __tablename__ = 'setting'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    test_amount = Column(Integer, nullable=False)


class UserTestingModel(Base):
    __tablename__ = 'user_testing'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    testing_id = Column(Integer, ForeignKey('testing.id'), nullable=False)


class UserTestAnswerModel(Base):
    __tablename__ = 'user_test_answer'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    answer_id = Column(Integer, ForeignKey('answer.id'), nullable=False)
    test_id = Column(Integer, ForeignKey('test.id'), nullable=False)


class AnswerModel(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    test_id = Column(Integer, ForeignKey('test.id'), nullable=False)
    is_correct = Column(Boolean, nullable=False)


class ResultModel(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    testing_id = Column(Integer, ForeignKey('testing.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

