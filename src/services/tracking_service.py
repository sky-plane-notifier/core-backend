from config.db import SessionDep, Session, get_session
from entities.dtos.tracking_dto import TrackingRequest, TrackingResponse, MatchingFlightResponse
from entities.dtos.flight_dto import FlightInfo, FlightResponse
from entities.models.tracking_model import Tracking, TrackingFilter
from sqlmodel import select
from fastapi import HTTPException
from services import flight_service
from typing import Dict, List
import schedule
from utilities.websockets.connection_manager import get_ws_manager



def get_trackings(session: SessionDep) -> List[TrackingResponse]:
    trackings = session.exec(select(Tracking)).all()
    return trackings

def get_tracking(tracking_id: int, session: SessionDep) -> TrackingResponse:
    tracking = session.get(Tracking, tracking_id)
    if not tracking:
       raise HTTPException(status_code=404, detail="Tracking not found")
    return tracking

def create_tracking(tracking: TrackingRequest, session: SessionDep) -> TrackingResponse:
    tracking_filter_db = TrackingFilter.model_validate(tracking.filter)
    tracking_db = Tracking(filter=tracking_filter_db, price=tracking.price)

    session.add(tracking_db)
    session.commit()
    session.refresh(tracking_db)

    return tracking_db

def update_tracking(tracking_id: int, tracking: TrackingRequest, session: SessionDep) -> TrackingResponse:
    tracking_db = session.get(Tracking, tracking_id)
    if not tracking_db:
        raise HTTPException(status_code=404, detail="Tracking not found")

    tracking_data = tracking.filter.model_dump(exclude_unset=True)
    tracking_db.filter.sqlmodel_update(tracking_data)
    tracking_db.price = tracking.price
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


def get_flight_matches(session: SessionDep | Session) -> Dict[int, MatchingFlightResponse]:

    flight_matches = {}
    trackings = session.exec(select(Tracking).where(Tracking.resolved != True)).all()
    for tracking in trackings:
        tracking_flight_matches = []

        flight_info = FlightInfo(**tracking.filter.model_dump(exclude="fly_date"), fly_date=tracking.filter.fly_date.strftime("%Y-%m-%d"))

        # Call flight service to get flights
        flights = flight_service.get_flights(flight_info)
        for flight in flights:
            try:
                price = int(flight.get("price", "MAD -1").replace('\xa0', ' ').split(" ")[1])
            except IndexError:
                price = -1
            if 0 <= price <= tracking.price:
                flight_response = {
                    **flight
                }
                tracking_flight_matches.append(flight_response)

        if tracking_flight_matches:
            tracking_response = {
                "id": tracking.id,
                "price": tracking.price,
                "filter": {
                    **tracking.filter.model_dump(),
                    "fly_date": tracking.filter.fly_date.strftime("%Y-%m-%d"),
                    "return_date": tracking.filter.return_date.strftime("%Y-%m-%d") if tracking.filter.return_date else None
                }
            }
            flight_matches[tracking.id] = {
                "tracking_details": tracking_response,
                "flight_matches": tracking_flight_matches
            }
    
    return flight_matches 

def get_flight_matches_and_mark_resolved(session: SessionDep | Session) -> Dict[int, MatchingFlightResponse]:
    flight_matches = get_flight_matches(session)
    for tracking_id, match in flight_matches.items():
        tracking = session.get(Tracking, tracking_id)
        tracking.resolved = True
        session.add(tracking)
    session.commit()
    return flight_matches