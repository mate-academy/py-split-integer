import pytest

from app.split_integer import split_integer

TEST_CASES = [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5), (100, 7)]


def test_should_return_one_part_when_number_of_parts_is_one() -> None:
    assert split_integer(8, 1) == [8]


def test_should_return_equal_parts_when_value_equals_parts() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_return_zeros_when_value_less_than_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_split_equally_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_sorted_parts_when_not_divisible() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


@pytest.mark.parametrize("value, number_of_parts", TEST_CASES)
def test_should_return_exactly_number_of_parts_elements(
    value: int,
    number_of_parts: int,
) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize("value, number_of_parts", TEST_CASES)
def test_should_return_difference_between_parts_not_more_than_one(
    value: int,
    number_of_parts: int,
) -> None:
    parts = split_integer(value, number_of_parts)
    assert max(parts) - min(parts) <= 1


@pytest.mark.parametrize("value, number_of_parts", TEST_CASES)
def test_should_return_parts_sorted_ascending(
    value: int,
    number_of_parts: int,
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


@pytest.mark.parametrize("value, number_of_parts", TEST_CASES)
def test_should_return_parts_with_sum_equal_to_value(
    value: int,
    number_of_parts: int,
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value
