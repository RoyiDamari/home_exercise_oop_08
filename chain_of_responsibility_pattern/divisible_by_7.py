from prime_number_handler import PrimeNumberHandler
from typing import override


class DivisibleBy7(PrimeNumberHandler):

    @override
    def handle(self, number):
        if number % 7 == 0:
            print(f"{number}: The number is not prime (divisible by 7)")
            return
        if self.next:
            self.next.handle(number)