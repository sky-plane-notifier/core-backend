import datetime
from typing import Optional
from sqlmodel import Field, Relationship, Column
from sqlalchemy import DateTime
from config.db import SQLModel
from entities.base.tracking_base import TrackingFilterBase


class TrackingFilter(TrackingFilterBase, table=True):
    id: int = Field(default=None, primary_key=True)
    fly_date: datetime.date
    return_date: Optional[datetime.date] = None
    
    tracking_id: int = Field(default=None, foreign_key="tracking.id", ondelete="CASCADE")


class Tracking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(sa_column=Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now))
    price: float
    resolved: bool = Field(default=False, nullable=True)

    filter: TrackingFilter = Relationship(cascade_delete=True)



