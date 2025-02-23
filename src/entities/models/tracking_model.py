from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, Column
from sqlalchemy import DateTime
from config.db import SQLModel
from entities.base.tracking_base import TrackingFilterBase


class TrackingFilter(TrackingFilterBase, table=True):
    id: int = Field(default=None, primary_key=True)

    tracking_id: int = Field(default=None, foreign_key="tracking.id", ondelete="CASCADE")


class Tracking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(sa_column=Column(DateTime, default=datetime.now, onupdate=datetime.now))
    price: float

    filter: TrackingFilter = Relationship(cascade_delete=True)



