import pytest


from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(15, 3) == [5, 5, 5]


@pytest.mark.parametrize(
    "value, parts, result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (15, 3, [5, 5, 5]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (2, 3, [0, 1, 1]),
        (7, 3, [2, 2, 3])
    ]
)
def test_result_properties_for_various_inputs(
    value: int,
    parts: int,
    result: list,
) -> None:
    assert len(split_integer(value, parts)) == parts
    assert all(isinstance(x, int) for x in split_integer(value, parts))
    assert split_integer(value, parts) == sorted(split_integer(value, parts))
    assert (max(split_integer(value, parts))
            - min(split_integer(value, parts)) <= 1)
    assert sum(
        1 for x in split_integer(value, parts)
        if x == min(split_integer(value, parts)) + 1
    ) == value % parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(16, 4) == [4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(5, 1) == [5]
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]
