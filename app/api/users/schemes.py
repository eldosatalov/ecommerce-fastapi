from __future__ import annotations

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    full_name: str


class UserSerializer(BaseModel):
    id: str
    full_name: str

    class Config:
        orm_mode = True
