""" Isogram - Solution """

from re import sub

def is_isogram(string: str) -> bool:
    """
    :param string: String to be verified if isogram or not.
    """

    string = sub(r'\W+', '', string).lower()
    return len(set(string)) == len(string)
