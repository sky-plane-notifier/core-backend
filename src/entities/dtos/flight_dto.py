from typing import Optional
from config.db import SQLModel

    
class FlightInfo(SQLModel):
    fly_date: str
    from_airport: str
    to_airport: str
    trip_type: str
    cabin_class: str
    nb_adults: int
    nb_children: int
    nb_infants_in_seat: int
    nb_infants_on_lap: int


class Airline(SQLModel):
    name: str
    website: str

class FlightResponse(SQLModel):
    is_best: bool
    departure_time: str
    arrival_time: str
    arrival_time_ahead: str
    duration: str
    stops: int
    delay: Optional[str]
    airline: Airline
    price: str
