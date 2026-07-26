from app.split_integer import split_integer
import pytest


class TestSplitInteger:

    @pytest.mark.parametrize(
        "value,parts",
        [
            (8, 1),
            (6, 2),
            (17, 4),
            (32, 6),
        ],
        ids=[
            "sum of parts should be 8",
            "sum of parts should be 6",
            "sum of parts should be 17",
            "sum of parts should be 32"
        ]
    )
    def test_difference_between_max_and_min_is_at_most_one(self, value, parts):
        parts_list = split_integer(value, parts)
        assert max(parts_list) - min(parts_list) <= 1, f"difference btw max and min number should be <= 1"


    @pytest.mark.parametrize(
        "value,parts",
        [
            (8, 1),
            (6, 2),
            (17, 4),
            (32, 6),
        ],
        ids=[
            "sum of parts should be 8",
            "sum of parts should be 6",
            "sum of parts should be 17",
            "sum of parts should be 32"
        ]
    )
    def test_sum_of_the_parts_should_be_equal_to_value(self, value, parts) -> None:
        assert sum(split_integer(value, parts)) == value, f"sum of parts does not equal {value}"


    @pytest.mark.parametrize(
        "value,parts,parts_list",
        [
            (9, 3, [3, 3, 3]),
            (16, 4, [4, 4, 4, 4]),
            (25, 5, [5, 5, 5, 5, 5])
        ],
        ids=[
            "all parts and their amount should equal 3",
            "all parts and their amount should equal 4",
            "all parts and their amount should equal 5"
        ]
    )
    def test_should_split_into_equal_parts_when_value_divisible_by_parts(self, value, parts, parts_list) -> None:
        act_parts_list = split_integer(value, parts)
        assert len(act_parts_list) == parts, f"number of parts should equal {parts}"
        assert parts_list == act_parts_list, f"parts is different from {parts}"


    @pytest.mark.parametrize(
    "value,parts",
        [
            (1, 1),
            (5, 1),
            (10, 1),
            (100, 1),
        ],
        ids=[
            "result should be [1]",
            "result should be [5]",
            "result should be [10]",
            "result should be [100]"
        ]
    )
    def test_should_return_part_equals_to_value_when_split_into_one_part(self, value, parts) -> None:
        parts_list = split_integer(value, parts)
        assert len(parts_list) == 1, f"result should contain 1 part"
        assert parts_list == [value], f"result does not equal {value}"


    @pytest.mark.parametrize(
        "value,parts,parts_list",
        [
            (17, 4, [4, 4, 4, 5]),
            (32, 6, [5, 5, 5, 5, 6, 6]),
        ],
        ids=[
            "result should be [4, 4, 4, 5]",
            "result should be [5, 5, 5, 5, 6, 6]"
        ]
    )
    def test_parts_should_be_sorted_when_they_are_not_equal(self, value, parts, parts_list) -> None:
        assert parts_list == split_integer(value, parts), f"{parts} should be sorted"


    @pytest.mark.parametrize(
       "value,parts,parts_list",
       [
           (1, 2, [0, 1]),
           (3, 4, [0, 1, 1, 1]),
           (10, 11, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
       ],
       ids=[
           "result should be [0, 1]",
           "result should be [0, 1, 1, 1]",
           "result should be [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"
       ]
    )
    def test_should_add_zeros_when_value_is_less_than_number_of_parts(self, value, parts, parts_list) -> None:
        assert split_integer(value, parts) == parts_list, f"result should be [0, 1, 1, ... 1]"
