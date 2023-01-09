from fastapi import APIRouter, Depends

from services.auth import schemas
from services.auth.deps import require_user

user_router = APIRouter()


@user_router.get('/me', summary="Users me")
async def me(user=Depends(require_user)):
    return schemas.UsersMeSchema(
        id=user.id,
        email=user.email
    )
