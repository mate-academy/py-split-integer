import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, summ",
    [
        (8, 1, 8),
        (6, 2, 6),
        (17, 4, 17),
        (32, 6, 32)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int, parts: int, summ: int
) -> None:
    assert (sum(split_integer(value, parts)) == summ), \
        (f"Sum of split list number {value} to "
         f"{parts} parts should be equal to {summ}")


@pytest.mark.parametrize(
    "value, parts, equal",
    [
        (8, 1, 8),
        (6, 2, 3),
        (21, 7, 3),
        (105, 5, 21)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int, parts: int, equal: int
) -> None:
    equal_list = split_integer(value, parts)
    assert (equal_list.count(equal) == len(equal_list)), \
        (f"list of divisible by parts {value} by "
         f"{parts} should be {[equal] * len(equal_list)}")


@pytest.mark.parametrize(
    "value, one, same",
    [
        (0, 1, 0),
        (8, 1, 8),
        (13, 1, 13),
        (1, 1, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int, one: int, same: int
) -> None:
    assert (split_integer(value, one) == [same]), \
        "value divided by 1 should be the same in list"


@pytest.mark.parametrize(
    "value, parts, sorted_list",
    [
        (7, 2, [3, 4]),
        (2, 3, [0, 1, 1]),
        (21, 5, [4, 4, 4, 4, 5]),
        (107, 3, [35, 35, 37])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int, parts: int, sorted_list: list
) -> None:
    split_list = split_integer(value, parts)
    assert (split_list == sorted(split_list)), \
        "Parts should be sorted when they are not equal"


@pytest.mark.parametrize(
    "value, parts, zeros",
    [
        (2, 7, 5),
        (2, 3, 1),
        (4, 6, 2)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, parts: int, zeros: int
) -> None:
    split_list = split_integer(value, parts)
    assert (split_list.count(1) == value and split_list.count(0) == zeros), \
        "List should have zeros when value is less than number of parts"
