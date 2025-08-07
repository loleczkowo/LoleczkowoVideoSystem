from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator
from passlib.hash import bcrypt
from sqlalchemy.exc import IntegrityError
from app.db import AsyncSessionLocal
from app.models import User
from logging_sys import logger
import re

# ill disable flake because fuck him
# flake8: noqa

router = APIRouter(prefix="/api", tags=["auth"])

USERNAME_REGEX = re.compile(r"^[A-Za-z0-9_]{3,25}$")
PWD_REGEX = re.compile(
    r"""^
        (?=.*[A-Za-z])         # at least one letter
        (?=.*\d)               # at least one digit
        (?=.*[^A-Za-z0-9])     # at least one special char
        [A-Za-z\d\W]{5,64}$    # allowed chars & length
    """,
    re.VERBOSE,
)


class SignupReq(BaseModel):
    display_name: str = Field(..., min_length=3, max_length=25)
    nickname:     str
    email:        EmailStr
    password:     str

    # ───── custom validators ─────
    @field_validator("nickname")
    @classmethod
    def nickname_rules(cls, v: str) -> str:
        if not USERNAME_REGEX.fullmatch(v):
            raise ValueError(
                "nickname 3-25 chars; letters, numbers, '_' only"
            )
        return v

    @field_validator("password")
    @classmethod
    def password_rules(cls, v: str) -> str:
        if not PWD_REGEX.fullmatch(v):
            raise ValueError("password 5-64 chars; must include letter, number, special char")
        return v


@router.post("/signup")
async def signup(req: SignupReq):
    async with AsyncSessionLocal() as db:
        user = User(
            nickname      = req.nickname,
            display_name  = req.display_name,
            email         = req.email,
            password_hash = bcrypt.hash(req.password),
        )
        db.add(user)
        try:
            await db.commit()
        except IntegrityError:
            await db.rollback()
            logger.debug(f"NICKNAME_OR_EMAIL_TAKEN")
            raise HTTPException(400, "NICKNAME_OR_EMAIL_TAKEN")
    logger.debug(f"ACC_CREATED ({req.nickname})")
    return {"result": "ACC_CREATED"}
