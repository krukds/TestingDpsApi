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

