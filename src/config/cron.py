import schedule
import asyncio
from services import job_service


scheduler = schedule.Scheduler()
loop = asyncio.get_event_loop()

def logger_job():
    print(scheduler.jobs)
    


scheduler.every(1).minutes.do(lambda: loop.create_task(job_service.tracking_notifier_job()))
scheduler.every(1).minutes.do(logger_job)

__all__ = [scheduler]