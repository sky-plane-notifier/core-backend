from config.db import SQLModel
from entities.base.tracking_base import TrackingFilterBase
from entities.dtos.flight_dto import FlightResponse
from typing import List



class TrackingFilterRequest(TrackingFilterBase):
    pass

class TrackingRequest(SQLModel):
    price: float

    filter: TrackingFilterRequest


class TrackingFilterResponse(TrackingFilterBase):
    id: int
    
    tracking_id: int 

class TrackingResponse(SQLModel):
    id: int
    price: float

    filter: TrackingFilterResponse

class MatchingFlightResponse(SQLModel):
    tracking_details: TrackingResponse
    flight_matches: List[FlightResponse] = []
