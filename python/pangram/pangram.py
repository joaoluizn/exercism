import re

def is_pangram(sentence):
    """
    :param str sentence: Given sentence to validate
    :rtype: bool
    """
    sentence = set(re.sub('[^A-Za-z]', '', sentence).lower())
    return True if len(sentence) == 26 else False
