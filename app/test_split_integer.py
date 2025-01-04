import pytest

from app.split_integer import split_integer


class TestsSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,result",
        [
            (8, 1, [8]),
            (6, 2, [3, 3]),
            (17, 4, [4, 4, 4, 5]),
            (32, 6, [5, 5, 5, 5, 6, 6])
        ]
    )
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            value: int,
            number_of_parts: int,
            result: list
    ) -> None:
        assert sum(split_integer(value, number_of_parts)) == value

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        split = split_integer(value, number_of_parts)
        assert all(part == split[0] for part in split)

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        split = split_integer(value, number_of_parts)
        assert split == [value]

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        split = split_integer(value, number_of_parts)
        assert split == sorted(split)

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        split = split_integer(value, number_of_parts)
        assert len(split) == number_of_parts
        assert split.count(0) == (number_of_parts - value)
