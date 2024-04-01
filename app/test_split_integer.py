import pytest
from app.split_integer import split_integer


class TestSplit:

    @pytest.mark.parametrize(
        "first_int, second_int, result",
        [
            (8, 1, [8]),
            (6, 2, [3, 3]),
            (17, 4, [4, 4, 4, 5]),
            (32, 6, [5, 5, 5, 5, 6, 6])
        ]
    )
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            first_int: int,
            second_int: int,
            result: list
    ) -> None:
        assert split_integer(first_int, second_int) == \
               result, f"Sum of the parts should be equal to value {first_int}"

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self
    ) -> None:
        first_int = 6
        second_int = 2
        assert split_integer(first_int, second_int) == [3, 3],\
            "Test should split into equal parts when value is divisible by"

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self
    ) -> None:
        first_int = 8
        second_int = 1
        assert split_integer(first_int, second_int) == [8],\
            "Test should return part equals to value when split into one part"

    def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
        first_int = 17
        second_int = 4
        result = [4, 4, 4, 5]
        assert split_integer(first_int, second_int) == sorted(result),\
            "Test parts should be sorted when they are not equal"

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self
    ) -> None:
        first_int = 3
        second_int = 5
        assert split_integer(first_int, second_int) == [0, 0, 1, 1, 1],\
            "Test should add zeros when value is less than number of parts"
