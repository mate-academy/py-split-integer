import unittest
from app.split_integer import split_integer


class TestSplit(unittest.TestCase):

    def test_split_integer_zero_parts(self) -> None:
        """
        Test for split_integer function with zero parts.
        """
        value = 10
        number_of_parts = 0
        expected_result = []
        self.assertEqual(
            split_integer(value, number_of_parts),
            expected_result
        )

    def test_split_integer_negative_value(self) -> None:
        """
        Test for split_integer function with a negative value.
        """
        value = -10
        number_of_parts = 3
        expected_result = [-4, -3, -3]
        self.assertEqual(
            split_integer(value, number_of_parts),
            expected_result
        )

    def test_split_integer_large_value(self) -> None:
        """
        Test for split_integer function with a large value.
        """
        value = 1000
        number_of_parts = 5
        expected_result = [200, 200, 200, 200, 200]
        self.assertEqual(
            split_integer(value, number_of_parts),
            expected_result
        )

    def test_split_integer_single_part(self) -> None:
        """
        Test for split_integer function with a single part.
        """
        value = 10
        number_of_parts = 1
        expected_result = [10]
        self.assertEqual(
            split_integer(value, number_of_parts),
            expected_result
        )

    def test_split_integer_decimal_value(self) -> None:
        """
        Test for split_integer function with a decimal value.
        """
        value = 7
        number_of_parts = 3
        expected_result = [2, 2, 3]
        self.assertEqual(
            split_integer(value, number_of_parts),
            expected_result
        )
