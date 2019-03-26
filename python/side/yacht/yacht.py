from collections import Counter
# Score categories
# Change the values as you see fit
YACHT = lambda x: 50 if x.count(x[0]) == 5 else 0
ONES = lambda x: x.count(1)
TWOS = lambda x: 2 * x.count(2)
THREES = lambda x: 3 * x.count(3)
FOURS = lambda x: 4 * x.count(4)
FIVES = lambda x: 5 * x.count(5)
SIXES = lambda x: 6 * x.count(6)
FULL_HOUSE = lambda x: sum(x) if len(Counter(x).values()) == 2 and 3 in Counter(x).values() else 0   
FOUR_OF_A_KIND = lambda x: x[0] * 4 if x.count(x[0]) >= 4 else (x[-1] * 4 if x.count(x[-1]) >= 4 else 0)
LITTLE_STRAIGHT = lambda x: 30 if sorted(x) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda x: 30 if sorted(x) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda x: sum(x)

def score(dice, category):
    """ Validate yacht round score """
    return category(dice)
