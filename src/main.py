from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import flight_router, tracking_router, airport_router
from contextlib import asynccontextmanager
from utilities.threading.background import run_in_background
from config.cron import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_event = run_in_background(scheduler.run_pending)
    yield
    scheduler.clear()
    run_event.stop() 

app = FastAPI(lifespan=lifespan)
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



app.include_router(flight_router.router)
app.include_router(tracking_router.router)
app.include_router(airport_router.router)