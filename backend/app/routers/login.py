import secrets
import hashlib
import datetime as dt
from fastapi import APIRouter
from pydantic import BaseModel
from passlib.hash import bcrypt
from sqlalchemy import select
from app.db import AsyncSessionLocal
from app.models import User, Connection
from logging_sys import logger


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
            return {"result": "ACC_NOT_EXIST"}
        if not bcrypt.verify(req.password, user.password_hash):
            return {"result": "WRONG_PASSWORD"}

        raw = secrets.token_hex(32)
        token_hash = hashlib.sha256(raw.encode()).hexdigest()

        db.add(Connection(
            token_hash=token_hash,
            user_id=user.id,
            created_at=dt.datetime.now(dt.timezone.utc),
            last_used=dt.datetime.now(dt.timezone.utc)
        ))
        await db.commit()
        return {"result": "ACC_LOGGED_IN", "token": raw}
