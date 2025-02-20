from entities.base.tracking_base import Tracking_Filter_Base
from config.db import SQLModel



class Tracking_Filter_Request(Tracking_Filter_Base):
    pass

class Tracking_Request(SQLModel):
    filter: Tracking_Filter_Request


class Tracking_Filter_Response(Tracking_Filter_Base):
    id: int
    
    tracking_id: int 

class Tracking_Response(SQLModel):
    id: int
    filter: Tracking_Filter_Response

