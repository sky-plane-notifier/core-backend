import fast_flights
from enums.airline_enum import Airline
from entities.dtos.flight_dto import Flight_Info


def get_flights(flight_info: Flight_Info):
    result: fast_flights.Result = fast_flights.get_flights(
        flight_data=[
            fast_flights.FlightData(date=flight_info.date, from_airport=flight_info.from_airport, to_airport=flight_info.to_airport)
        ],
        trip=flight_info.trip_type,
        seat=flight_info.cabin_class,
        passengers=fast_flights.Passengers(
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
    