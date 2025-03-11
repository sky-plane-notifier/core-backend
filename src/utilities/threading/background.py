import threading
import time


def run_in_background(func, interval=10, *args, **kwargs):
    
    class BackgroundEvent(threading.Event):
        def stop(self):
            self.set()
        
        def is_stopped(self):
            return self.is_set()

    run_event = BackgroundEvent()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            if interval <= 0:
                func(*args, **kwargs)
                return
            
            while not run_event.is_stopped():
                print("Running background function => ", func.__name__)
                func(*args, **kwargs)
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()

    return run_event