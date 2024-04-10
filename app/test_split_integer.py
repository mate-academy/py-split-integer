import unittest
from app.split_integer import split_integer


class TestSplit(unittest.TestCase):

    def test_split_integer_zero_parts(self) -> None:
        """
        Test for split_integer function with zero parts.
        """
        self.assertEqual(
            split_integer(10, 0), [],
            "Value must be divided into an empty list"
            " when the number of parts is zero."
        )

    def test_split_integer_negative_value(self) -> None:
        """
        Test for split_integer function with a negative value.
        """
        self.assertEqual(
            split_integer(-10, 3), [-4, -3, -3],
            "Value must be divided into parts of approximately equal size,"
            " even with negative values."
        )

    def test_split_integer_large_value(self) -> None:
        """
        Test for split_integer function with a large value.
        """
        self.assertEqual(
            split_integer(1000, 5), [200, 200, 200, 200, 200],
            "Large value must be divided into equal parts."
        )

    def test_split_integer_single_part(self) -> None:
        """
        Test for split_integer function with a single part.
        """
        self.assertEqual(
            split_integer(10, 1), [10],
            "Value must be divided into a list"
            " with a single element equal to the original value."
        )

    def test_split_integer_decimal_value(self) -> None:
        """
        Test for split_integer function with a decimal value.
        """
        self.assertEqual(
            split_integer(7, 3), [2, 2, 3],
            "Value must be divided into parts of approximately equal size."
        )
