""" Module to calculate Difference of Squares """

from collections.abc import Generator

def square_of_sum(number: int) -> int:
    """ Calculate square of the sum of a sequence starting in 1 up to a given Number """
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """ Calculate sum of squares for the sequence starting in 1 up to a given Number """

    def square_generator(number: int) -> Generator:
        for value in range(1, number + 1):
            yield value ** 2

    return sum(square for square in square_generator(number))


def difference_of_squares(number: int) -> int:
    """ Calculate difference of squares for the sequence starting in 1 up to a given Number """
    return square_of_sum(number) - sum_of_squares(number)
