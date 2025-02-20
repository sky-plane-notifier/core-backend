from fastapi import APIRouter
from config.db import SessionDep
from services import tracking_service
from entities.dtos.tracking_dto import Tracking_Response, Tracking_Request


router = APIRouter(prefix="/trackings", tags=["trackings"])


@router.get("")
def get_trackings(session: SessionDep) -> list[Tracking_Response]:
    return tracking_service.get_trackings(session)

@router.post("")
def create_tracking(tracking: Tracking_Request, session: SessionDep) -> Tracking_Response:
    return tracking_service.create_tracking(tracking, session)

@router.get("/{tracking_id}")
def get_tracking(tracking_id: int, session: SessionDep) -> Tracking_Response:
    return tracking_service.get_tracking(tracking_id, session)

@router.put("/{tracking_id}")
def update_tracking(tracking_id: int, tracking: Tracking_Request, session: SessionDep) -> Tracking_Response:
    return tracking_service.update_tracking(tracking_id, tracking, session)

@router.delete("/{tracking_id}")
def delete_tracking(tracking_id: int, session: SessionDep) -> bool:
    return tracking_service.delete_tracking(tracking_id, session)