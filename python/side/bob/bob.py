""" Bob Side Execise Solution """

import re
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
    is_upper_message = hey_bob.isupper()
    is_question = len(hey_bob) > 0 and hey_bob[-1] == '?'

    if is_upper_message and is_question:
        answer = 'Calm down, I know what I\'m doing!'
    elif is_question:
        answer = 'Sure.'
    elif is_upper_message:
        answer = 'Whoa, chill out!'
    elif re.findall("[\r\t]", hey_bob) or hey_bob == '':
        answer = 'Fine. Be that way!'

    return answer
