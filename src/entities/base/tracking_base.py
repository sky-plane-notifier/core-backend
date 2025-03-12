
from enums.flight_enum import Cabin_Type_Enum, Trip_Type_Enum
from config.db import SQLModel


class TrackingFilterBase(SQLModel):
    from_airport: str
    to_airport: str
    cabin_class: Cabin_Type_Enum
    trip_type: Trip_Type_Enum
    nb_adults: int
    nb_children: int
    nb_infants_in_seat: int
    nb_infants_on_lap: int