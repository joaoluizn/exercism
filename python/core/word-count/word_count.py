""" Word Count Solution """

from collections import Counter
from re import sub


def count_words(sentence: str) -> dict:
    """ Count words occurrences in given string """

    clear_sentence = sub(r'[^\w\'\-]|_', ' ', sentence)
    apostrophes_ready_sentence = [
        word.strip("'")
        for word in clear_sentence.lower().split()
    ]
    return dict(Counter(apostrophes_ready_sentence))
