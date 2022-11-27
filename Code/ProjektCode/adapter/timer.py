"""
imports
"""
from datetime import datetime
from .interfaces import Timeable

class Timer(Timeable):
    """
    global variables
    """
    def __init__(self):
        self.second_in_milli = 1000000
        self.minute_in_sec = 60

    """
    functions
    """
    def allow_passes_per_second(self, passes):
        time_to_wait = self.second_in_milli / passes
        current_millisec = datetime.now().microsecond
        end_time = int(current_millisec + time_to_wait)
        if end_time >= self.second_in_milli:
            end_time = end_time - self.second_in_milli
            while end_time <= datetime.now().microsecond:
                pass
            while end_time >= datetime.now().microsecond:
                pass
        else:
            while end_time >= datetime.now().microsecond:
                pass
        
    def blocking_wait_seconds(self, seconds):
        current_seconds = datetime.now().second
        end_time = int(current_seconds + seconds)
        if end_time >= self.minute_in_sec:
            end_time = end_time - self.minute_in_sec
            while end_time <= datetime.now().second:
                pass
            while end_time >= datetime.now().second:
                pass
        else:
            while end_time >= datetime.now().second:
                pass