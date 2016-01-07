#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Methods to solve project euler problems

This module exposes implementations to solve project euler problems that can be
found at https://projecteuler.net/archives. Solutions shown in this module are
adapted from http://www.s-anand.net/euler.html

Example:
    You can run the entire module at once, to solve many problems at the same
    time:
        python project_euler.py

    Or you can import a single method tu use it:
        from project_euler import calculate_multiples_sum
        res = calculate_multiples_sum([3, 5], 1000)
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os


def calculate_multiples_sum(multiples, limit):
    """Calculate the sum of numbers that are multiples of "multiples".

    Args:
        multiples (list): List of multiples like [3, 5].
        limit (int): Maximum number value to be added.

    Returns:
        int: Sum of "multiples" that are less than limit.
    """

    n = 0
    for i in xrange(1, limit + 1):
        for multiple in multiples:
            if i % multiple == 0:
                n += i
                continue

    return n


def calculate_fibonacci_sum(limit, even_or_uneven=None):
    """Calculate the sum of numbers of the Fibonacci sequence.

    Args:
        limit (int): Maximum number value to be added.
        even_or_uneven (str): "even" will add only even numbers from the
            Fibonacci sequence, "uneven" will add uneven numbers. If None, all
            number will be added.
    Returns:
        int: Sum of Fibonacci numbers below limit.
    """

    if even_or_uneven and even_or_uneven == "even":
        return sum((i for i in _fib_generator(limit) if i % 2 == 0))

    elif even_or_uneven and even_or_uneven == "uneven":
        return sum((i for i in _fib_generator(limit) if i % 2 != 0))

    elif even_or_uneven is None:
        return sum(_fib_generator(limit))

    else:
        raise Exception(even_or_uneven, "is not a valid input.")


def _fib_generator(limit):
    """Generator of Fibonacci numbers up to a limit.

    Args:
        limit (int): Maximum value number to be generated.

    Yields:
        int: Number of the Fibonacci sequence.
    """

    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def calculate_largest_prime_factor(n):
    """Calculate the largest prime factor of a number.

    Args:
        n (int): A number.

    Returns:
        int: The largest prime factor of n.
    """

    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1

    return n


def main():
    print("Problem 1: Sum of multiples of 3 and 5, below 1000")
    print(calculate_multiples_sum([3, 5], 1000), "\n")

    print("Problem 2: Sum of even Fibonacci numbers, below 4M")
    print(calculate_fibonacci_sum(4000000, "even"), "\n")

    print("Problem 3: Largest prime factor of 600851475143")
    print(calculate_largest_prime_factor(600851475143), "\n")

if __name__ == '__main__':
    main()
