import secrets
import hashlib
from fastapi import APIRouter
from pydantic import BaseModel
from passlib.hash import bcrypt
from sqlalchemy import select
from app.db import AsyncSessionLocal
from app.models import User, Connection
from logging_sys import logger
from helpers import utc_naive_now

router = APIRouter(prefix="/api", tags=["auth"])


class LoginReq(BaseModel):
    identifier: str   # nickname OR email
    password:   str


class LoginRes(BaseModel):
    result: str
    token:  str | None = None


@router.post("/login", response_model=LoginRes)
async def login(req: LoginReq):
    logger.debug("user try to log!")
    async with AsyncSessionLocal() as db:
        res = await db.execute(
            select(User).where(
                (User.nickname == req.identifier) | (
                    User.email == req.identifier)
            )
        )
        user: User | None = res.scalar()

        if user is None:
            logger.debug("ACCOUNT NOT EXIST")
            return {"result": "ACC_NOT_EXIST"}
        if not bcrypt.verify(req.password, user.password_hash):
            logger.debug("BAD PASSWORD")
            return {"result": "WRONG_PASSWORD"}

        raw = secrets.token_hex(32)
        token_hash = hashlib.sha256(raw.encode()).hexdigest()

        db.add(Connection(
            token_hash=token_hash,
            user_id=user.id,
            created_at=utc_naive_now(),
            last_used=utc_naive_now()
        ))
        await db.commit()
        logger.debug("GOOD")
        return {"result": "ACC_LOGGED_IN", "token": raw}
