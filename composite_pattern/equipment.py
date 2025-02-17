from abc import ABC, abstractmethod


class Equipment(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_child(self, equipment):
        pass

    @abstractmethod
    def remove_child(self, equipment):
        pass

    @abstractmethod
    def get_contents(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

