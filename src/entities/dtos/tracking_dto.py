from config.db import SQLModel
from entities.base.tracking_base import TrackingFilterBase
from entities.dtos.flight_dto import FlightResponse
from typing import List
import datetime
from typing import Optional



class TrackingFilterRequest(TrackingFilterBase):
    fly_date: datetime.date
    return_date: Optional[datetime.date] = None

class TrackingRequest(SQLModel):
    price: float

    filter: TrackingFilterRequest


class TrackingFilterResponse(TrackingFilterBase):
    id: int
    fly_date: str | datetime.date
    return_date: Optional[str | datetime.date] = None
    
    tracking_id: int 

class TrackingResponse(SQLModel):
    id: int
    price: float
    resolved: bool

    filter: TrackingFilterResponse

class MatchingFlightResponse(SQLModel):
    tracking_details: TrackingResponse
    flight_matches: List[FlightResponse] = []

class MinimalMatchingFlightResponse(SQLModel):
    tracking_details: TrackingResponse
    flight_match: FlightResponse
