""" Bob Side Execise Solution """

from functools import wraps


def strip_input(func):
    """
    Simple Decorator to strip single arg function input

    :param func: A function to be decorated
    """
    @wraps(func)
    def wrapper(string):
        return func(string.strip())
    return wrapper


@strip_input
def response(hey_bob):
    """
    Returns the bob answer to a given message

    :param hey_bob: A message for bob
     """
    answer = 'Whatever.'
    if hey_bob == '':
        answer = 'Fine. Be that way!'
    elif hey_bob.isupper():
        if hey_bob[-1] == '?':
            answer = 'Calm down, I know what I\'m doing!'
        else:
            answer = 'Whoa, chill out!'
    elif hey_bob[-1] == '?':
        answer = 'Sure.'

    return answer
