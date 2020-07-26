from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):


    @abstractmethod
    def v_menu(self):
        pass

    @abstractmethod
    def v_board(self):
        pass

    @abstractmethod
    def v_statistics(self):
        pass
