import pytest

from app.split_integer import split_integer

SPLIT_CASES = [
    (8, 1),
    (6, 2),
    (17, 4),
    (32, 6),
    (1, 2),
]


@pytest.mark.parametrize("value, number_of_parts", SPLIT_CASES)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    assert sum(result) == value


@pytest.mark.parametrize("value, number_of_parts", SPLIT_CASES)
def test_number_of_parts_should_match_requested_amount(
    value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts


@pytest.mark.parametrize("value, number_of_parts", SPLIT_CASES)
def test_difference_between_max_and_min_part_should_not_exceed_one(
    value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    assert max(result) - min(result) <= 1


@pytest.mark.parametrize("value, number_of_parts", SPLIT_CASES)
def test_parts_should_be_sorted_ascending(
    value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 8
    num_parts = 2
    result = split_integer(value, num_parts)

    assert result == [4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    num_parts = 1
    result = split_integer(value, num_parts)

    assert result[0] == value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    num_parts = 2
    result = split_integer(value, num_parts)

    assert result == [0, 1]
