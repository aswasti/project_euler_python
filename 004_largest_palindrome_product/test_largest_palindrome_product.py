import unittest
import pytest  # type: ignore
from largest_palindrome_product import largest_palindrome_product

class LargestPalindromeProductTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_largest_palindrome_product_example(self):
        actual_result = largest_palindrome_product()
        error_message = ('Called largest_prime_factor().'
                         f'The function returned {actual_result}, but the '
                         f'tests expected 906609.')
        self.assertEqual(actual_result, 906609, msg=error_message)

if __name__ == '__main__':
    unittest.main()
