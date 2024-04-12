import unittest
from app.split_integer import split_integer


class TestSplit(unittest.TestCase):

    def test_sum_of_the_parts_should_be_equal_to_value(
            self
    ) -> None:
        assert split_integer(8, 1) == [8],\
            "Value must be divided into a list with 1 element equal to value."

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self
    ) -> None:
        assert split_integer(6, 2) == [3, 3], \
            "Even value must be divided into two parts of equal size."

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self
    ) -> None:
        assert split_integer(17, 4) == [4, 4, 4, 5],\
            "Odd value must be divided into four parts" \
            " with a difference of 1."

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self
    ) -> None:
        assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6],\
            "Large value must be divided into six parts" \
            " with a difference of 1."

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self
    ) -> None:
        assert split_integer(5, 3) == [1, 2, 2], \
            "Value must be divided into three parts with a difference of 1."
