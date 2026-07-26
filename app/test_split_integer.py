import pytest
from typing import List
from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, expected",
        [
            pytest.param(
                8, 1, [8],
                id="should_split_into_one_part"
            ),
            pytest.param(
                6, 2, [3, 3],
                id="should_split_into_equal_parts"
            ),
            pytest.param(
                17, 4, [4, 4, 4, 5],
                id="should_be_sorted_and_differ_by_maximum_one"
            ),
            pytest.param(
                32, 6, [5, 5, 5, 5, 6, 6],
                id="should_handle_large_numbers_correctly"
            ),
            pytest.param(
                21, 4, [5, 5, 5, 6],
                id="sum_of_parts_should_equal_value"
            )
        ])
    def test_split_integer_is_working_properly(
            self,
            value: int,
            number_of_parts: int,
            expected: List[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == expected
