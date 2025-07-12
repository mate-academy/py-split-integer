import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(8, 1)
    assert sum(result) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(25, 5)
    assert all(part == result[0] for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 4)
    assert result == [0, 0, 1, 1]


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (14, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ],
    ids=[
        "test with one number division",
        "test division two part",
        "division four part",
        "division on six part"
    ],
)
def number_of_parts(value: int,
                    number_of_parts: int,
                    result: list) -> None:

    assert split_integer(value, number_of_parts) == result


def test_max_near_min() -> None:
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


def rest_on_len_list() -> None:
    result = split_integer(14, 4)
    assert len(result) == 4
