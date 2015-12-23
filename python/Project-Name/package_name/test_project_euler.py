#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests methods to solve project euler problems."""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import unittest
import nose

import project_euler as pe


class ProjectEulerTestCase(unittest.TestCase):
    """Tests for Project Euler methods."""

    def test_calculate_multiples_sum(self):
        """Tests sum of multiples."""

        multiples = [3]
        limit = 3
        res = pe.calculate_multiples_sum(multiples, limit)
        exp = 3

        self.assertEqual(res, exp)

    def test_calculate_fibonacci_sum(self):
        """Tests sum of fibonacci numbers."""

        res = pe.calculate_fibonacci_sum(1)
        exp = 2
        self.assertEqual(res, exp)

        res = pe.calculate_fibonacci_sum(2)
        exp = 4
        self.assertEqual(res, exp)

        res = pe.calculate_fibonacci_sum(4)
        exp = 7
        self.assertEqual(res, exp)

    def test_calculate_largest_prime_factor(self):
        """Tests calculation of largest prime factor of a number."""

        res = pe.calculate_largest_prime_factor(7)
        exp = 7
        self.assertEqual(res, exp)

        res = pe.calculate_largest_prime_factor(13)
        exp = 13
        self.assertEqual(res, exp)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
