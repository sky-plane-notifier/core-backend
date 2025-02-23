from fastapi import APIRouter
from config.db import SessionDep
from services import tracking_service
from entities.dtos.tracking_dto import TrackingResponse, TrackingRequest, MatchingFlightResponse
from typing import Dict, List


router = APIRouter(prefix="/trackings", tags=["trackings"])


@router.get("")
def get_trackings(session: SessionDep) -> List[TrackingResponse]:
    return tracking_service.get_trackings(session)

@router.get("/matches")
def get_flight_matches(session: SessionDep) ->  Dict[int, MatchingFlightResponse]:
    return tracking_service.get_flight_matches(session)

@router.post("")
def create_tracking(tracking: TrackingRequest, session: SessionDep) -> TrackingResponse:
    return tracking_service.create_tracking(tracking, session)

@router.get("/{tracking_id}")
def get_tracking(tracking_id: int, session: SessionDep) -> TrackingResponse:
    return tracking_service.get_tracking(tracking_id, session)

@router.put("/{tracking_id}")
def update_tracking(tracking_id: int, tracking: TrackingRequest, session: SessionDep) -> TrackingResponse:
    return tracking_service.update_tracking(tracking_id, tracking, session)

@router.delete("/{tracking_id}")
def delete_tracking(tracking_id: int, session: SessionDep) -> bool:
    return tracking_service.delete_tracking(tracking_id, session)