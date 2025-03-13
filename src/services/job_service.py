from services.tracking_service import get_minimal_flight_matches_for_notification
from utilities.websockets.connection_manager import get_ws_manager
from config.db import get_session


async def tracking_notifier_job():
    print("Running tracking_job to notify with matching flights")
    with next(get_session()) as session:
        flight_matches = get_minimal_flight_matches_for_notification(session)
        ws_manager = get_ws_manager()
        await ws_manager.send_json("edg", flight_matches)