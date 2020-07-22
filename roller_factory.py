from typing import List

from roller import Roller
from dicer import Dicer
from modifier import Modifier


class RollerFactory():


    @staticmethod
    def create_roller_by_string(in_roll_str: str="2d8 3d6 7") -> List[Roller]:
        new_rolls = list()

        for roll_clips in in_roll_str.split():
            print("roll_clips", roll_clips)

            roll_di = roll_clips.split("d")
            print(roll_di)

            if len(roll_di) < 2:
                new_rolls.append(Modifier(int(roll_di[0])))

            else:
                for x in range(int(roll_di[0])):
                    new_rolls.append(Dicer(int(roll_di[1])))

        return new_rolls 


if __name__ == '__main__':
    x = RollerFactory()

    y = RollerFactory.create_roller_by_string()

    for i in y:
        print(i)
