from datetime import datetime
from math import pow

def add_gigasecond(moment):
    """ Add one gigasecond to a specific moment """
    return datetime.fromtimestamp(moment.timestamp() + pow(10, 9))
