from prime_number_handler import PrimeNumberHandler
from typing import override


class PrimeNumber(PrimeNumberHandler):

    @override
    def handle(self, number):
        print(f"{number}: The number is prime!")

