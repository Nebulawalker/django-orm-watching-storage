import time

def format_duration(duration):
    duration_in_seconds = time.gmtime(duration)
    formatted_duration = time.strftime("%H ч %M мин", duration_in_seconds)
    return formatted_duration