import unittest
import pytest  # type: ignore
from smallest_multiple import smallest_multiple

class SmallestMultipleTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_smallest_multiple_example_01(self):
        actual_result = smallest_multiple(10)
        expected_result = 2520
        error_message = ('Called smallest_multiple(10).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_smallest_multiple_example_02(self):
        actual_result = smallest_multiple(20)
        expected_result = 232792560
        error_message = ('Called smallest_multiple(20).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected 232792560.')
        self.assertEqual(actual_result, expected_result, msg=error_message)
if __name__ == '__main__':
    unittest.main()
    
