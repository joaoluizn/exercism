""" Isogram - Solution """

def is_isogram(string: str) -> bool:
    """
    :param string: String to be verified if isogram or not.
    """
    visited_letters = set()
    word_generator = (k.lower() for k in string if k.isalpha())
    for letter in word_generator:
        if letter in visited_letters:
            return False
        else:
            visited_letters.add(letter)
    return True
