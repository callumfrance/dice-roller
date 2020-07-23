from typing import List

from roller import Roller
from dicer import Dicer
from modifier import Modifier


class RollerFactory():


    @staticmethod
    def create_roller_by_string(in_roll_str: str="2d8 - 3d6 + 7 + 2d4 - 6") -> List[Roller]:
        """
        **Not fully implemented**

        1. Remove all whitespace
        2. Split along '-'
        3. For each '-' string, split along '+'
        4. Add a '-' sign to the first element of each '-' list except all[0]
        5. Add a '+' sign to all other elements of each '-' list
        6. Create dice using 'd' or modifier if not using 'd'
        """
        new_rolls = list()
        raw_rolls = list()
        sign_sequence = list() # list of either '-' or '+' corresponding to roll

        in_roll_str = "".join(in_roll_str.split()) # Removes all whitespace
        minus_split = in_roll_str.split("-")
        sign_sequence = ['+'] + ['-'] * (len(minus_split) - 1)

        print("Pre-Adding:", minus_split, sign_sequence)

        sign_sentinel = 0
        for _ in minus_split:
            print("Next in minus_split: ", _)
            for n, plus_split in enumerate(_.split("+")):
                # TODO Requires fixing array values for a proper insertion...
                raw_rolls.append(plus_split)
                temp_sentinel = sign_sentinel + 1
                print("\tplus_split: ", plus_split, "\t\t", sign_sentinel, temp_sentinel)

                print("\t\t", sign_sequence[:sign_sentinel], "[+]", sign_sequence[sign_sentinel + 1:],)

                if n != 0:
                    sign_sequence = sign_sequence[:sign_sentinel] + \
                            ["+"] + \
                            sign_sequence[sign_sentinel + 1:]

                print("\t\t", sign_sequence)

                sign_sentinel = temp_sentinel + 1

        print(raw_rolls, sign_sequence)

        for _ in raw_rolls:
            roll_di = _.split("d")

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
