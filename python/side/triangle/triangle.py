""" Triangle - Solution """

from collections import Counter

def is_equilateral(sides: list) -> bool:
    """
    Calculate if triangle formed by sides is equilateral or not

    :param sides: Sides to be validated
    """
    if sum(sides) == 0:
        return False

    if len(Counter(sides)) == 1:
        return True
    return False

def is_isosceles(sides: list) -> bool:
    """
    Calculate if trangle formed by sides is isosceles or not

    :param sides: Sides to be validated
    """
    if is_triangle(sides):
        if len(Counter(sides)) == 2 or is_equilateral(sides):
            return True
        return False
    return False

def is_scalene(sides: list) -> bool:
    """
    Calculate if triangle formed by sides is scalene

    :param sides: Sides to be validated
    """
    if is_triangle(sides):
        if len(Counter(sides)) == 3:
            return True
        return False
    return False

def is_triangle(sides: list) -> bool:
    """
    Calculate if sides generate a valid triangle

    :param sides: Sides to be validated
    """
    a_side, b_side, c_side = sides
    if a_side + b_side <= c_side or\
        b_side + c_side <= a_side or\
        c_side + a_side <= b_side:
        return False
    return True
