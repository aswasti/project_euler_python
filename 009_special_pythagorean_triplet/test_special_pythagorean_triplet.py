import unittest
import pytest  # type: ignore
from special_pythagorean_triplet import special_pythagorean_triplet

class SpecialPythagoreanTripletTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_special_pythagorean_triplet_01(self):
        actual_result = special_pythagorean_triplet()
        expected_result = 31875000
        error_message = ('Called largest_product(4).'
                         f'The function returned {actual_result}, but the '
                         f'tests expected {expected_result}.')      
        self.assertEqual(actual_result, expected_result, msg=error_message)
if __name__ == '__main__':
    unittest.main()
    
