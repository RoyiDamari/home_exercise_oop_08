from range_check import  RangeCheck
from divisible_by_2 import DivisibleBy2
from divisible_by_3 import DivisibleBy3
from divisible_by_5 import DivisibleBy5
from divisible_by_7 import DivisibleBy7
from prime_number import PrimeNumber

def main():

     range_check = RangeCheck()
     divisible_by_2 = DivisibleBy2()
     divisible_by_3 = DivisibleBy3()
     divisible_by_5 = DivisibleBy5()
     divisible_by_7 = DivisibleBy7()
     prime_number = PrimeNumber()
     chain_root = range_check

     range_check.next = divisible_by_2
     divisible_by_2.next = divisible_by_3
     divisible_by_3.next = divisible_by_5
     divisible_by_5.next = divisible_by_7
     divisible_by_7.next = prime_number
     prime_number.next = None

     try:
          divisible_by_3.next = None  # This should raise ValueError
     except ValueError as e:
          print(f"Expected Error: {e}")

     try:
          divisible_by_5.next = "InvalidObject"  # Should raise TypeError
     except TypeError as e:
          print(f"Expected Error: {e}")

     try:
          divisible_by_7.next = divisible_by_7  # Should raise ValueError (self-referencing)
     except ValueError as e:
          print(f"Expected Error: {e}")

     test_numbers = [17, 23, 100, 121, 169, "hello", 99.5]  # Last two should fail

     for num in test_numbers:
          try:
               print(f"\nChecking number: {num}")
               chain_root.handle(num)
               print("-" * 50)
          except ValueError as e:
               print(f"Value Error: {e}")  # Handles numbers out of range
          except TypeError as e:
               print(f"Typing error: {e}")  # Handles invalid numbers (non-integers)
          except Exception as e:
               print(f"Unexpected Error in Processing Number: {e}") # Handles all the unexpected cases


if __name__ == "__main__":
     main()