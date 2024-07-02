# test_sum_of_multiples.py

import unittest
import pytest 
from sum_of_multiples import sum_of_multiples

class SumOfMultiplesTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_sum_of_multiples_example_01(self):
        actual_result = sum_of_multiples(1000, 3, 5)
        error_message = ('Called sum_of_multiples(1000, 3, 5).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 233168.')
        self.assertEqual(actual_result, 233168, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sum_of_multiples_example_02(self):
        actual_result = sum_of_multiples(10, 3, 5)
        error_message = ('Called sum_of_multiples(10, 3, 5).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 23.')
        self.assertEqual(actual_result, 23, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_sum_of_multiples_example_03(self):
        actual_result = sum_of_multiples(1, 3, 5)
        error_message = ('Called sum_of_multiples(1, 3, 5).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 0.')
        self.assertEqual(actual_result, 0, msg=error_message)

if __name__ == '__main__':
    unittest.main()
