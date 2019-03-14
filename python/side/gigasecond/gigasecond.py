from datetime import datetime

def add_gigasecond(moment):
    """ Add one gigasecond to a specific moment """
    return datetime.fromtimestamp(moment.timestamp() + 10**9)
