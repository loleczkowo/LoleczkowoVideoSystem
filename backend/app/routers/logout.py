from fastapi import APIRouter, Response, Request
from sqlalchemy import delete
from app.session_utils import _hash
from app.db import AsyncSessionLocal
from app.models import Connection
from logging_sys import logger

router = APIRouter(prefix="/api", tags=["auth"])


@router.post("/logout")
async def logout(request: Request, response: Response):
    raw_token = request.cookies.get("lvs_token")
    if raw_token is not None:
        token_hash = await _hash(raw_token)

        async with AsyncSessionLocal() as db:
            await db.execute(
                delete(Connection).where(Connection.token_hash == token_hash)
            )
            await db.commit()
            logger.debug("LOGOUT: token removed from Connection (if existed)")

    # Always delete cookie, even if invalid
    response.delete_cookie(
        key="lvs_token",
        path="/",
        samesite="lax",
        secure=True,
        httponly=True
    )
    return {"result": "LOGGED_OUT"}
