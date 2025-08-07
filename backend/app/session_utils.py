import hashlib
from fastapi import HTTPException, status, Request
from sqlalchemy import select, update
from app.db import AsyncSessionLocal
from app.models import Connection, User
from logging_sys import logger
from helpers import utc_naive_now


async def _hash(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


async def check_session(request: Request) -> int:

    raw_token = request.cookies.get("lvs_token")

    if raw_token is None:
        logger.debug("NO SIESSION")
        raise HTTPException(status_code=401, detail="no session")

    token_hash = await _hash(raw_token)

    async with AsyncSessionLocal() as db:
        res = await db.execute(
            select(Connection.user_id).where(
                Connection.token_hash == token_hash)
        )
        row = res.first()
        if row is None:
            logger.debug("SESSION INVALID")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="invalid session")

        user_id = row[0]

        await db.execute(
            update(Connection)
            .where(Connection.token_hash == token_hash)
            .values(last_used=utc_naive_now())
        )
        await db.commit()
        logger.debug(f"SESSION VALID: {user_id}")
        return user_id


async def is_mod(user_id: int) -> bool:
    async with AsyncSessionLocal() as db:
        res = await db.execute(
            select(User.is_mod).where(User.id == user_id)
        )
        return bool(res.scalar())


async def check_mod(uid):
    if not await is_mod(uid):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="moderator perms required")
