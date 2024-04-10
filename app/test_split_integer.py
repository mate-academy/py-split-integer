import unittest
from app.split_integer import split_integer


class TestSplit(unittest.TestCase):

    def test_split_integer_single_value_single_part(self) -> None:
        assert split_integer(8, 1) == [8],\
            "Value must be divided into a list with 1 element equal to value."

    def test_split_integer_even_value_two_parts(self) -> None:
        assert split_integer(6, 2) == [3, 3],\
            "Even value must be divided into two parts of equal size."

    def test_split_integer_odd_value_four_parts(self) -> None:
        assert split_integer(17, 4) == [4, 4, 4, 5],\
            "Odd value must be divided into four parts" \
            " with a difference of 1."

    def test_split_integer_large_value_six_parts(self) -> None:
        assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6],\
            "Large value must be divided into six parts" \
            " with a difference of 1."

    def test_split_integer_value_largest_part(self) -> None:
        assert split_integer(5, 3) == [1, 2, 2],\
            "Value must be divided into three parts with a difference of 1."
