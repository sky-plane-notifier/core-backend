from enum import Enum


class Cabin_Type_Enum(str, Enum):
    ECONOMY_CLASS = "economy"
    BUSINESS_CLASS = "business"

class Trip_Type_Enum(str, Enum):
    ONE_WAY = "one_way"
    RETURN = "return"