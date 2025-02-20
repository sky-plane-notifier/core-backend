from pydantic import BaseModel


class Passengers_Info(BaseModel):
    adults: int
    children: int
    infants_in_seat: int
    infants_on_lap: int
    
class Flight_Info(BaseModel):
    date: str
    from_airport: str
    to_airport: str
    trip_type: str
    cabin_class: str
    passengers_info: Passengers_Info

class AirportSearch(BaseModel):
    search: str
