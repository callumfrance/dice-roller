from roller import Roller

from modifier import Modifier
from dicer import Dicer


class Board():


    def __init__(self, dice=dict(), mods=list()):
        self.dice = dice
        self.mods = mods


    def add_roller(self, new_roller):
        if new_roller.isinstance(Modifier):
            self.mods.append(new_roller)
        elif new_roller.isinstance(Dicer):
            self.dice.setdefault(new_roller.sides, []).append(new_roller)

    def roll_all(self) -> int:
        total = 0
        total_replay = list()

        for i in self.mods:
            total_replay.append(i.roll())
            total += total_replay[-1]

        for key in self.dice:
            for j in self.dice[key]:
                total_replay.append(j.roll())
                total += total_replay[-1]

        return (total_replay, total)



if __name__ == '__main__':
    rollers = Board(dice={6: [Dicer(6), Dicer(6)]},
            mods=[Modifier(1), Modifier(3)])

    print(rollers)

    print(rollers.roll_all())
