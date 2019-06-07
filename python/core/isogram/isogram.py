""" Isogram - Solution """

from collections import Counter
from re import sub

def is_isogram(string: str) -> bool:
    """
    :param string: String to be verified if isogram or not.
    """
    counter = Counter(sub(r'\W+', '', string).lower())
    return all([i == 1 for i in counter.values()])
