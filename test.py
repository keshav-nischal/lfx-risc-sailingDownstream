import unittest
from main import is_length_divisible_by_10, get_values_at_indices_divisible_by_2_3

class TestProgram(unittest.TestCase):
    def test_is_length_divisible_by_10(self):
        self.assertTrue(is_length_divisible_by_10([1] * 10))  # Valid case
        self.assertFalse(is_length_divisible_by_10([1] * 8))  # Invalid case

    def test_get_values_at_indices_divisible_by_2_3(self):    
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected_result = [2, 6, 8, 12, 14, 18, 20]
        self.assertEqual(get_values_at_indices_divisible_by_2_3(input_list), expected_result)

if __name__ == '__main__':
    unittest.main()
