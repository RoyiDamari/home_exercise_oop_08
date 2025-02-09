from abc import ABC, abstractmethod


class PrimeNumberHandler(ABC):
    def __init__(self):
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if value is not None and not isinstance(value, PrimeNumberHandler):
            raise TypeError("Error: next must be an instance of PrimeNumberHandler or None")

        if value is self:  # Prevents infinite recursion
            raise ValueError("Error: A handler cannot reference itself as next")

        if value is None and self.__next is not None:
            raise ValueError("Error: Cannot set `None` in the middle of the chain!")

        self.__next = value

    @abstractmethod
    def handle(self, number):
        pass