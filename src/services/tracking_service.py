from config.db import SessionDep
from entities.dtos.tracking_dto import Tracking_Request, Tracking_Response
from entities.models.tracking_model import Tracking
from sqlmodel import select
from fastapi import HTTPException


def get_trackings(session: SessionDep) -> list[Tracking_Response]:
    trackings = session.exec(select(Tracking)).all()
    return trackings

def get_tracking(tracking_id: int, session: SessionDep) -> Tracking_Response:
    tracking = session.get(Tracking, tracking_id)
    if not tracking:
       raise HTTPException(status_code=404, detail="Tracking not found")
    return tracking

def create_tracking(tracking: Tracking_Request, session: SessionDep) -> Tracking_Response:
    tracking_db = Tracking.model_validate(tracking)

    session.add(tracking_db)
    session.commit()
    session.refresh(tracking_db)

    return tracking_db

def update_tracking(tracking_id: int, tracking: Tracking_Request, session: SessionDep) -> Tracking_Response:
    tracking_db = session.get(Tracking, tracking_id)
    if not tracking_db:
        raise HTTPException(status_code=404, detail="Tracking not found")

    tracking_data = tracking.filter.model_dump(exclude_unset=True)
    tracking_db.filter.sqlmodel_update(tracking_data)
    session.add(tracking_db.filter)
    session.commit()
    session.refresh(tracking_db.filter)

    return tracking_db

def delete_tracking(tracking_id: int, session: SessionDep) -> bool:
    tracking = session.get(Tracking, tracking_id)
    if not tracking:
        raise HTTPException(status_code=404, detail="Tracking not found")
    session.delete(tracking)
    session.commit()
    return True