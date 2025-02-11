from fast_flights import FlightData, Passengers, Result, get_flights, Flight
from pydantic import BaseModel
from enums.airlines import Airline


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




def list_flights(flight_info: Flight_Info):
    result: Result = get_flights(
        flight_data=[
            FlightData(date=flight_info.date, from_airport=flight_info.from_airport, to_airport=flight_info.to_airport)
        ],
        trip=flight_info.trip_type,
        seat=flight_info.cabin_class,
        passengers=Passengers(
            adults=flight_info.passengers_info.adults,
            children=flight_info.passengers_info.children,
            infants_in_seat=flight_info.passengers_info.infants_in_seat,
            infants_on_lap=flight_info.passengers_info.infants_on_lap
        ),
        fetch_mode="fallback",
    )

    flights = [{
        **flight.__dict__,
        "stops": flight.stops if type(flight.stops) == int else -1,
        "airline": {
            "name": flight.name,
            "website": Airline.search_by(flight.name)["website"]
        }} for flight in list(result.flights)]
    
    return list(flights)
    