import unittest
import pytest  # type: ignore
from get_primes import get_primes

class GetPrimesTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_get_primes_01(self):
        actual_result = get_primes(5)
        expected_result = [2,3,5]
        error_message = ('Called get_primes(5).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_get_primes_02(self):
        actual_result = get_primes(10)
        expected_result = [2,3,5,7]
        error_message = ('Called get_primes(10).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)
    
    @pytest.mark.task(taskno=3)
    def test_get_primes_03(self):
        actual_result = get_primes(20)
        expected_result = [2,3,5,7,11,13,17,19]
        error_message = ('Called get_primes(20).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)
if __name__ == '__main__':
    unittest.main()
    
