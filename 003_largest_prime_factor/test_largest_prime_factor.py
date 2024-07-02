import unittest
import pytest  # type: ignore
from largest_prime_factor import largest_prime_factor

class LargestPrimeFactorTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_largest_prime_factor_example(self):
        actual_result = largest_prime_factor(13195)
        error_message = ('Called largest_prime_factor(13195).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 29.')
        self.assertEqual(actual_result, 29, msg=error_message)

if __name__ == '__main__':
    unittest.main()
