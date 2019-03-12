import math

def score(x, y):
    """ Get Dart game score """
    distance = math.hypot(x, y)
    if distance <= 1:
        return 10
    elif 1 < distance <= 5:
        return 5
    elif 5 < distance <= 10:
        return 1
    else:
        return 0
