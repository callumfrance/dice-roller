from random import randint
from roller import Roller


class Dicer(Roller):


    def __init__(self, sides=6, style=None):
        self.sides = sides
        self.style = style

    def roll(self) -> int:
        return randint(1, self.sides)
