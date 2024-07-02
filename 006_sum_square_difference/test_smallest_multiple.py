import unittest
import pytest  # type: ignore
from sum_square_difference import sum_square_difference

class SumSquareDifferenceTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_sum_square_difference_example_01(self):
        actual_result = sum_square_difference(10)
        expected_result = 2640
        error_message = ('Called sum_square_difference(10).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sum_square_difference_example_02(self):
        actual_result = sum_square_difference(100)
        expected_result = 25164150
        error_message = ('Called sum_square_difference(100).'
                        f'The function returned {actual_result}, but the '
                        f'tests expected 232792560.')
        self.assertEqual(actual_result, expected_result, msg=error_message)
if __name__ == '__main__':
    unittest.main()
    
