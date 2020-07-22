from typing import Dict, Set, List

from roller import Roller
from roller_factory import RollerFactory


class RollerPacket():


    def __init__(self):
        self.rollers = list()

    def roll_all(self) -> Set[int, List[Set[int, Roller]]]:
        pass

    def statistics(self) -> Dict[int, float]:
        """Not completely implemented
        """
        totals = dict()
        
        for i in range(len(self.rollers) - 1): # Repeat for all rollers bar 1st
            temp_totals = dict()
            for j in self.rollers:
                for k in totals:
                    pass
            
            # https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python-taking-union-o
            merged_totals = {**totals, **temp_totals}
            totals = merged_totals

        return totals
