from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import flight_router, tracking_router, airport_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 


@app.get("/health1")
def health():
    return {"message": "Sky plane notifier is running!"}


app.include_router(flight_router.router)
app.include_router(tracking_router.router)
app.include_router(airport_router.router)