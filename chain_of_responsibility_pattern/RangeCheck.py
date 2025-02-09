from PrimeNumberHandler import PrimeNumberHandler
from typing import override


class RangeCheck(PrimeNumberHandler):

    @override
    def handle(self, number):

        # Ensure the input is an integer
        if not isinstance(number, int):
            raise TypeError(f"{number} is not a valid integer")

        # Check if it's in range 10-100
        if not (10 <= number <= 100):
            raise ValueError(f"{number}: The number is out of range (10-100)")

        if self.next:
            self.next.handle(number)

