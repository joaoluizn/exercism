""" scrabble score solution """

from collections import Counter

POINT_TABLE = {
    **dict.fromkeys(list('aeioulnrst'), 1),
    **dict.fromkeys(list('dg'), 2),
    **dict.fromkeys(list('bcmp'), 3),
    **dict.fromkeys(list('fhvwy'), 4),
    **dict.fromkeys(list('k'), 5),
    **dict.fromkeys(list('jx'), 8),
    **dict.fromkeys(list('qz'), 10)
}


def score(word) -> int:
    """ calculates the scrabble score for given word """
    word_counter = Counter(word.lower())
    point_list = [__get_scrabble_point(factor, letter) for letter, factor in word_counter.items()]
    return sum(point_list)


def __get_scrabble_point(factor, letter) -> int:
    """ gets the scrabble point for a given factor and letter """
    return factor * POINT_TABLE.get(letter, 0)

def test():
    score('qqqueirosjdfurieoqoqoqoqoqoqoqoooqoqoqoqoqjdsuwjdifiroelsazmcncbjsjsjsjsjajsdjaskdjadjakdjaskjdaksdkasjdakjsdasjkdajksdjkadjkasdjkajkdajksdjkasjkdajskdajksdjkajskdakdajksd'), 


if __name__ == "__main__":
    import timeit
    t = timeit.Timer("test()", setup="from __main__ import test")
    repeat_samples = t.repeat()
    print(f'the mean for the given code was: {sum(repeat_samples)/len(repeat_samples)} seconds.')
