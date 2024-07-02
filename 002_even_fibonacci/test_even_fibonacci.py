import unittest
import pytest # type: ignore
from even_fibonacci import even_fibonacci

class SumEvenFibonacciTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_sum_even_fibonacci_example(self):
        actual_result = even_fibonacci(4000000)
        error_message = ('Called sum_even_fibonacci(4000000).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 4613732.')
        self.assertEqual(actual_result, 4613732, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sum_even_fibonacci_small_limit(self):
        actual_result = even_fibonacci(10)
        error_message = ('Called sum_even_fibonacci(10).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 10.')
        self.assertEqual(actual_result, 10, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_sum_even_fibonacci_no_even_fibonacci(self):
        actual_result = even_fibonacci(1)
        error_message = ('Called sum_even_fibonacci(1).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 0.')
        self.assertEqual(actual_result, 0, msg=error_message)

if __name__ == '__main__':
    unittest.main()
