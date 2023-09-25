import pytest

from app.split_integer import split_integer


class TestSplitInteger:

    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
    ) -> None:
        value = 32
        number_of_parts = 6
        result = [5, 5, 5, 5, 6, 6]
        assert split_integer(value, number_of_parts) == result

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        self
    ) -> None:
        value = 10
        number_of_parts = 2
        result = [5, 5]
        assert split_integer(value, number_of_parts) == result

    def test_should_return_part_equals_to_value_when_split_into_one_part(
        self
    ) -> None:
        value = 10
        number_of_parts = 1
        result = [10]
        assert split_integer(value, number_of_parts) == result

    def test_parts_should_be_sorted_when_they_are_not_equal(
        self
    ) -> None:
        value = 15
        number_of_parts = 4
        result = [3, 4, 4, 4]
        assert split_integer(value, number_of_parts) == result

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        self
    ) -> None:
        value = 3
        number_of_parts = 5
        result = [0, 0, 1, 1, 1]
        assert split_integer(value, number_of_parts) == result
