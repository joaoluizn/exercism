""" DnD Character Creation Script """
from random import randint

def modifier(stat: int) -> int:
    """ Calculate the stat modifier for a stat """
    return (stat - 10) // 2

class Character:
    def __init__(self):
        self._abilities_names = {
            'strength', 
            'dexterity',
            'constitution', 
            'intelligence', 
            'wisdom', 
            'charisma',
        }
        [setattr(self, k, self.ability()) for k in self._abilities_names]
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """ Get random ability values based on four 6-sided dice rollls """
        return sum(sorted([randint(1,len(self._abilities_names)) for _ in range(4)])[1:])

