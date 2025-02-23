from pydantic import BaseModel
from typing import Optional


    
class FlightInfo(BaseModel):
    fly_date: str
    from_airport: str
    to_airport: str
    trip_type: str
    cabin_class: str
    nb_adults: int
    nb_children: int
    nb_infants_in_seat: int
    nb_infants_on_lap: int


class Airline(BaseModel):
    name: str
    website: str

class FlightResponse(BaseModel):
    is_best: bool
    departure_time: str
    arrival_time: str
    arrival_time_ahead: str
    duration: str
    stops: int
    delay: Optional[str]
    airline: Airline
    price: str
