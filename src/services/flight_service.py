import fast_flights
from enums.airline_enum import Airline
from entities.dtos.flight_dto import FlightInfo, FlightResponse
from typing import List


def get_flights(flight_info: FlightInfo) -> List[FlightResponse]:
    result: fast_flights.Result = fast_flights.get_flights(
        flight_data=[
            fast_flights.FlightData(date=flight_info.fly_date, from_airport=flight_info.from_airport, to_airport=flight_info.to_airport)
        ],
        trip=flight_info.trip_type,
        seat=flight_info.cabin_class,
        passengers=fast_flights.Passengers(
            adults=flight_info.nb_adults,
            children=flight_info.nb_children,
            infants_in_seat=flight_info.nb_infants_in_seat,
            infants_on_lap=flight_info.nb_infants_on_lap
        ),
        fetch_mode="fallback",
    )

    flights = [{
        **flight.__dict__,
        "departure_time": flight.departure,
        "arrival_time": flight.arrival,
        "stops": flight.stops if type(flight.stops) == int else -1,
        "airline": {
            "name": flight.name,
            "website": Airline.search_by(flight.name)["website"]
        }} for flight in list(result.flights)]
    
    return list(flights)
    