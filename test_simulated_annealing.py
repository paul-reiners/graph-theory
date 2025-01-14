import random
from unittest import TestCase
import unittest

from simulated_annealing import randomly_selected_successor


class Test(TestCase):
    def test_randomly_selected_successor(self):
        random.seed(10)
        current = {'m1': 'f8',
                   'm2': 'f6',
                   'm3': 'f4',
                   'm4': 'f1',
                   'm5': 'f3',
                   'm6': 'f2',
                   'm7': 'f7',
                   'm8': 'f5'}
        successor = randomly_selected_successor(current)
        value_diff_count = 0

        for key in current.keys() & successor.keys():
            if current[key] != successor[key]:
                value_diff_count += 1

        self.assertEqual(4, value_diff_count)


if __name__ == '__main__':
    unittest.main()
