from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from enums import airports
from helpers import flights
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 


@app.get("/health")
def health():
    return {"message": "Sky plane notifier is running!"}


@app.post("/flights")
def list_flights(flight_info: flights.Flight_Info, response: Response):
    try:
        return flights.list_flights(flight_info)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(e)
        return {"message": "An error occurred while processing the request."}


@app.get("/airports")
def list_airports():
    return [airport for airport in airports.Airport]

class AirportSearch(BaseModel):
    search: str

@app.post("/airports")
def list_airports_by(search_info: AirportSearch):
    if search_info.search == None or len(search_info.search.strip()) == 0:
        return list_airports()
    return airports.Airport.search_by(search_info.search)