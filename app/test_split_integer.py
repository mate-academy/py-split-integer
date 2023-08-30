import pytest
from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,result",
        [
            pytest.param(
                8, 2,
                [4, 4],
                id="test_sum_of_the_parts_should_be_equal_to_value"
            ),
            pytest.param(
                9, 3,
                [3, 3, 3],
                id="test_should_split_into_equal_parts_when_value_divisible_by_parts"
            ),
            pytest.param(
                8, 1,
                [8],
                id="test_should_return_part_equals_to_value_when_split_into_one_part"
            ),
            pytest.param(
                30, 4,
                [7, 7, 8, 8],
                id="test_parts_should_be_sorted_when_they_are_not_equal"
            ),
            pytest.param(
                1, 3,
                [0, 0, 1],
                id="test_should_add_zeros_when_value_is_less_than_number_of_parts"
            )
        ]
    )

    def test_split_integer(
            self,
            value: int,
            number_of_parts: int,
            result: list[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == result
