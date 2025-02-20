from fastapi import APIRouter
from enums import airport_enum


router = APIRouter(prefix="/airports", tags=["airports"])


@router.get("")
def get_airports(search: str | None = None):
    if search == None or len(search.strip()) == 0:
        return [airport for airport in airport_enum.Airport]
    return airport_enum.Airport.search_by(search)
