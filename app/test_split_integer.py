import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (1, 2), (5, 5), (100, 7)],
)
def test_sum_of_parts_should_be_equal_to_value(
    value: int, parts: int
) -> None:
    assert sum(split_integer(value, parts)) == value


@pytest.mark.parametrize(
    "value, parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (1, 2), (5, 5), (100, 7)],
)
def test_should_return_exact_number_of_parts(
    value: int, parts: int
) -> None:
    assert len(split_integer(value, parts)) == parts


@pytest.mark.parametrize(
    "value, parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (1, 2), (5, 5), (100, 7)],
)
def test_difference_between_parts_should_be_at_most_one(
    value: int, parts: int
) -> None:
    result = split_integer(value, parts)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (1, 2), (5, 5), (100, 7)],
)
def test_parts_should_be_sorted_ascending(
    value: int, parts: int
) -> None:
    result = split_integer(value, parts)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (1, 2)],
)
def test_parts_should_not_be_negative(value: int, parts: int) -> None:
    assert all(part >= 0 for part in split_integer(value, parts))


def test_should_return_equal_parts_when_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_value_when_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_distribute_remainder_over_last_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_less_than_parts() -> None:
    assert split_integer(1, 2) == [0, 1]
