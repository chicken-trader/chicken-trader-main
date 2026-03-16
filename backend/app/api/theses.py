from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.base import get_db
from app.models.entities import FollowedThesis, ThesisEvaluation, User
from app.schemas.thesis import ThesisOut
from app.services.thesis import reevaluate_active_theses


router = APIRouter(prefix="/theses", tags=["theses"])


@router.get("", response_model=list[ThesisOut])
def list_followed_theses(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> list[ThesisOut]:
    rows = db.query(FollowedThesis).filter(FollowedThesis.user_id == current_user.id).order_by(FollowedThesis.followed_at.desc()).all()
    output: list[ThesisOut] = []
    for row in rows:
        latest = (
            db.query(ThesisEvaluation)
            .filter(ThesisEvaluation.thesis_id == row.id)
            .order_by(ThesisEvaluation.evaluated_at.desc())
            .first()
        )
        output.append(
            ThesisOut(
                id=row.id,
                event_id=row.event_id,
                thesis_summary=row.thesis_summary,
                report_headline=row.report_headline,
                time_horizon=row.time_horizon,
                followed_at=row.followed_at,
                closed=row.closed,
                latest_state=latest.state.value if latest else "Active",
                latest_explanation=latest.explanation if latest else "No reevaluation yet",
            )
        )
    return output


@router.delete("/{thesis_id}", status_code=204)
def unfollow_thesis(
    thesis_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> None:
    thesis = db.get(FollowedThesis, thesis_id)
    if not thesis or thesis.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Thesis not found")
    db.delete(thesis)
    db.commit()


@router.post("/reevaluate")
def reevaluate(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> dict:
    _ = current_user
    count = reevaluate_active_theses(db)
    return {"evaluated": count}
