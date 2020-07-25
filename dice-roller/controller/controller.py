from abc import ABCMeta, abstractmethod


class Controller(metaclass=ABCMeta):


    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def base(self):
        pass

    @abstractmethod
    def process_roll(self):
        pass

    @abstractmethod
    def change_layout(self):
        pass

