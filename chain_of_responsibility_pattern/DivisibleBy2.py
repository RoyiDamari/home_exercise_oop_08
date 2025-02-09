from PrimeNumberHandler import PrimeNumberHandler
from typing import override


class DivisibleBy2(PrimeNumberHandler):

    @override
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number}: The number is not prime (divisible by 2)")
            return
        if self.next:
            self.next.handle(number)