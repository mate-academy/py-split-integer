import pytest
from app.split_integer import split_integer


# def test_sum_of_the_parts_should_be_equal_to_value() -> None:
#     value, number_of_parts = 6, 2
#     parts = split_integer(value, number_of_parts)
#     assert sum(parts) == value
#
#
# def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
#     value, number_of_parts = 10, 2
#     parts = split_integer(value, number_of_parts)
#     assert parts == [5, 5]
#
#
# def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
#     value, number_of_parts = 10, 1
#     parts = split_integer(value, number_of_parts)
#     assert parts == [10]
#
#
# def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
#     value, number_of_parts = 10, 3
#     parts = split_integer(value, number_of_parts)
#     assert parts == sorted(parts)
#
#
# def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
#     value, number_of_parts = 1, 3
#     parts = split_integer(value, number_of_parts)
#     assert parts == [0, 0, 1]

@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (9, 3, [3, 3, 3]),
        (10, 3, [3, 3, 4]),
        (7, 3, [2, 2, 3]),
        (5, 5, [1, 1, 1, 1, 1]),
        (4, 5, [0, 1, 1, 1, 1]),
    ],
)
def test_various_scenarios(value, number_of_parts, expected):
    parts = split_integer(value, number_of_parts)
    assert parts == expected