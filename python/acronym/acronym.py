import re

def abbreviate(words):
    """
    :param str sentence: Given sentence to abbreviate
    :rtype: bool
    """
    pre = re.sub('[^A-Za-z ]', '', words.replace('-', ' '))
    return re.sub('[^A-Z]', '', pre.lower().title())
