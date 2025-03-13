from fastapi import APIRouter
from fastapi import status, Response
from services import flight_service
from entities.dtos.flight_dto import FlightInfo, FlightResponse
from typing import List



router = APIRouter(prefix="/flights", tags=["flights"])


@router.post("")
def get_flights(flight_info: FlightInfo, response: Response) -> List[FlightResponse]:
    try:
        return flight_service.get_flights(flight_info)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(e)
        return {"message": "An error occurred while processing the request."}