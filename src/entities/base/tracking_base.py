import datetime
from typing import Optional
from config.db import SQLModel
from enums.flight_enum import Cabin_Type_Enum, Trip_Type_Enum

class TrackingFilterBase(SQLModel):
    from_airport: str
    to_airport: str
    cabin_class: Cabin_Type_Enum
    trip_type: Trip_Type_Enum
    fly_date: datetime.date
    return_date: Optional[datetime.date] = None
    nb_adults: int
    nb_children: int
    nb_infants_in_seat: int
    nb_infants_on_lap: int