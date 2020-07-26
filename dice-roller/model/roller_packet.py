from typing import Dict, Tuple, List

from .roller import Roller


class RollerPacket():


    def __init__(self):
        self.rollers = list()

    def add_rollers(self, in_roll_data: str, in_seg_fact):
        new_rollers = in_seg_fact.create_roller_by_string(in_roll_data)

        for x in new_rollers:
            self.rollers.append(x)

    def roll_all(self) -> Tuple[int, List[Tuple[int, Roller]]]:
        """
        :return: A tuple that contains:
            - The integer total that has been rolled
            - A list of every Roller's total that was rolled, plus that Roller
        :rtype: Tuple
        """
        total = 0
        rolled = list()

        for i in self.rollers:
            rolled.append((i.roll(), i))
            total += rolled[-1][0]

        return (total, rolled)

    def statistics(self) -> Dict[int, float]:
        """
        Determines the probabililty of a number being rolled from RollerPacket

        All of the probabilities, when summed, should equal 1.0

        :return: A dictionary where the key is the number that was rolled, and
            the value is the decimal probablility that is was rolled (out of 1).
        :rtype: Dict
        """
        all_probs = list()
        total_prob = dict()

        for i in self.rollers:
            all_probs.append(i.probability_dist())

        total_prob = all_probs.pop(0)

        while len(all_probs) > 0:
            last_probs = total_prob
            next_probs = all_probs.pop(0)
            total_prob = dict()

            for lp_key in last_probs:
                for np_key in next_probs:
                    semi_total = total_prob.get(lp_key + np_key, 0)
                    total_prob[lp_key + np_key] = semi_total + \
                            (last_probs[lp_key] * next_probs[np_key])

        return total_prob


if __name__ == '__main__':
    from roller_factory import RollerFactory

    rp = RollerPacket()
    rf = RollerFactory()

    rp.rollers = rf.create_roller_by_string("3d4 2d6 5")
    print(rp.rollers)

    run = rp.roll_all()

    print(run[0])

    for x in run[1]:
        print(x[0], end="\t")

        print(type(x[1]), "\t", vars(x[1]))
        # if isinstance(x[1], Dicer):
        #     print("d", x[1].sides, end="")
        # if isinstance(x[1], Modifier):
        #     print("M", x[1].value, end="")


    stats = rp.statistics()

    stat_1 = 0

    for key in stats:
        stat_1 += stats[key]

    print("stat_1 is ", stat_1)
    print(stats)
