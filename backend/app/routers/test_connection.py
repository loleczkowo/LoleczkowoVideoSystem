from fastapi import APIRouter, Request
from app.db import AsyncSessionLocal
from app.models import User
from logging_sys import logger
from app.session_utils import check_session

router = APIRouter(prefix="/api", tags=["auth"])


@router.get("/test-connection")
async def test_connection(request: Request):
    user_id = await check_session(request)

    async with AsyncSessionLocal() as db:
        user = await db.get(User, user_id)

        if not user:
            logger.error(f"User {user_id} not found in DB")
            return {"result": "USER_NOT_FOUND"}

        return {
            "result": "VALID_SESSION",
            "user": {
                "id": user.id,
                "nickname": user.nickname,
                "display_name": user.display_name,
                "description": user.description,
                "email": user.email,
                "is_mod": user.is_mod,
            }
        }
