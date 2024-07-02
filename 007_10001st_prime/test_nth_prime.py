import unittest
import pytest  # type: ignore
from nth_prime import nth_prime

class NthPrimeTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_nth_prime_example_01(self):
        actual_result = nth_prime(10001)
        expected_result = 104743
        error_message = ('Called nth_prime(10001).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)

if __name__ == '__main__':
    unittest.main()
    
