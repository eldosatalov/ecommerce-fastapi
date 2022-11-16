from logging import getLogger
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users.schemes import UserSerializer, UserSchema
from app.models import User
from app.database import db
router = APIRouter(prefix="/v1/users")

logger = getLogger(__name__)


@router.post("/", response_model=UserSerializer)
async def create(user: UserSchema):
    user = User(**user.dict())
    await user.save(db)
    return user


@router.get("/", response_model=List[UserSerializer])
async def create():
    users = await User.get_all(db)
    return users
