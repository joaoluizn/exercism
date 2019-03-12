import random
import string

class Robot(object):
    def __init__(self):
        self.alphabeat = list(string.ascii_uppercase)
        self.random_gen = random.Random()
        self.reset()

    def reset(self):
        """ Resets Robot Serial Name """
        self.name = ''.join(
            [self.random_gen.choice(self.alphabeat),
            self.random_gen.choice(self.alphabeat),
            '{:03}'.format(self.random_gen.choice(range(1, 1000)))])
