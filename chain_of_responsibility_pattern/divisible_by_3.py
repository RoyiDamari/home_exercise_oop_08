from prime_number_handler import PrimeNumberHandler
from typing import override


class DivisibleBy3(PrimeNumberHandler):

    @override
    def handle(self, number):
        if number % 3 == 0:
            print(f"{number}: The number is not prime (divisible by 3)")
            return
        if self.next:
            self.next.handle(number)