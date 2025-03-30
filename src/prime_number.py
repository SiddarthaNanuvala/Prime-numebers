"""
Prime Number Checker Module.

This module provides a function to determine whether a given number is a prime number.
It includes an optimized algorithm to check for prime numbers efficiently.

Functions:
    - is_prime_number(in_number): Returns True if in_number is a prime number, otherwise False.
"""
import string
import math

def is_prime_number(in_number):
    """Check if a number is a prime number."""

    # 1 and numbers less than 1 are not prime numbers
    if in_number <= 1:
        return False

    # 2 and 3 are prime numbers
    if in_number <= 3:
        return True

    # Eliminate even numbers and numbers divisible by 3
    if in_number % 2 == 0 or in_number % 3 == 0:
        return False

    # Check divisibility from 5 to sqrt(n), skipping even numbers
    for i in range(5, int(math.sqrt(in_number)) + 1, 6):
        if in_number % i == 0 or in_number % (i + 2) == 0:
            return False

    return True
