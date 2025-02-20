from fastapi import APIRouter
from fastapi import status, Response
from services import flight_service


router = APIRouter(prefix="/flights", tags=["flights"])


@router.post("")
def get_flights(flight_info: flight_service.Flight_Info, response: Response):
    try:
        return flight_service.get_flights(flight_info)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(e)
        return {"message": "An error occurred while processing the request."}