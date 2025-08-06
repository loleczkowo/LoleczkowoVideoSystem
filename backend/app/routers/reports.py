from fastapi import APIRouter, Request
from sqlalchemy import select
from app.db import AsyncSessionLocal
from app.models import Report
from app.session_utils import check_mod, check_session

router = APIRouter(prefix="/api/reports", tags=["reports"])


@router.get("/oldest")
async def oldest_report(request: Request):
    uid = await check_session(request)
    await check_mod(uid)

    async with AsyncSessionLocal() as db:
        res = await db.execute(
            select(Report).order_by(Report.time_of_report.asc()).limit(1)
        )
        rep = res.scalar()

    if rep is None:
        return {"detail": "no reports"}

    return {
        "id": rep.id,
        "report_type": rep.report_type,
        "target_id": rep.target_id,
        "reported_by": rep.reported_by,
        "time_of_report": rep.time_of_report.isoformat(),
        "reason": rep.reason,
    }
