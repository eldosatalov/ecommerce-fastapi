from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(
        "id", Integer(), autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    full_name = Column(String)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f"full_name={self.full_name}, "
            f")>"
        )
