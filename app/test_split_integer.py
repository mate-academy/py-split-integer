# from app.split_integer import split_integer
#
#
# class TestSplitInteger:
#     def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
#         assert (
#             sum(split_integer(32, 6)) == 32
#         ), "Sum of parts should be equal to value"
#
#     def test_should_split_into_equal_parts_when_value_divisible_by_parts(
#         self,
#     ) -> None:
#         assert split_integer(6, 2) == [
#             3,
#             3,
#         ], "Should_split_into_equal_parts_when_value_divisible_by_parts"
#
#     def test_should_return_part_equals_to_value_when_split_into_one_part(
#         self,
#     ) -> None:
#         assert split_integer(8, 1) == [
#             8
#         ], "should_return_part_equals_to_value_when_split_into_one_part"
#
#     def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
#         assert split_integer(32, 6) == [
#             5,
#             5,
#             5,
#             5,
#             6,
#             6,
#         ], "parts_should_be_sorted_when_they_are_not_equal"
#
#     def test_should_add_zeros_when_value_is_less_than_number_of_parts(
#         self,
#     ) -> None:
#         assert split_integer(3, 6) == [
#             0,
#             0,
#             0,
#             1,
#             1,
#             1,
#         ], "should_add_zeros_when_value_is_less_than_number_of_parts"

import pytest
from app.split_integer import split_integer
from typing import List


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="parts_should_be_sorted_when_they_are_not_equal",
        ),
        pytest.param(
            6,
            2,
            [3, 3],
            id="Should_split_into_equal_parts_when_value_divisible_by_parts",
        ),
        pytest.param(
            8,
            1,
            [8],
            id="should_return_part_equals_to_value_when_split_into_one_part",
        ),
        pytest.param(
            3,
            6,
            [0, 0, 0, 1, 1, 1],
            id="should_add_zeros_when_value_is_less_than_number_of_parts",
        ),
    ],
)
def test_split_integer(value: int, parts: int, expected: List[int]) -> None:
    assert split_integer(value, parts) == expected
