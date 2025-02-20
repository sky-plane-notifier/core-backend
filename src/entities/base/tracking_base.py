import datetime
from typing import Optional
from sqlmodel import Field
from config.db import SQLModel
from enums.flight_enum import Cabin_Type_Enum, Trip_Type_Enum

class Tracking_Filter_Base(SQLModel):
    origin: str
    destination: str
    cobin_type: Cabin_Type_Enum
    trip_type: Trip_Type_Enum
    fly_date: datetime.date
    return_date: Optional[datetime.date]
    nb_adults: int
    nb_children: int
    nb_infants_on_seat: int
    nb_infants_on_lap: int
    price: float