from roller import Roller


class Modifier(Roller):


    def __init__(self, value=1, style=None):
        self.value = value
        self.style = None

    def roll(self) -> int:
        return self.value
