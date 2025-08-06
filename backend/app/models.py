import datetime as dt
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id:            Mapped[int] = mapped_column(primary_key=True)
    nickname:      Mapped[str] = mapped_column(unique=True)
    display_name:  Mapped[str]
    email:         Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    description:   Mapped[str | None]
    balance:       Mapped[float] = mapped_column(default=0.0)
    blocked_since: Mapped[dt.datetime | None]
    is_mod:        Mapped[bool] = mapped_column(default=False)


class Connection(Base):
    __tablename__ = "connections"

    token_hash: Mapped[str] = mapped_column(primary_key=True)
    user_id:    Mapped[int]
    created_at: Mapped[dt.datetime]
    last_used:  Mapped[dt.datetime]


class Report(Base):
    __tablename__ = "reports"

    id:             Mapped[int] = mapped_column(primary_key=True)
    report_type:    Mapped[str]
    target_id:      Mapped[int]
    reported_by:    Mapped[int]
    time_of_report: Mapped[dt.datetime]
    reason:         Mapped[str]
