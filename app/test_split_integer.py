import pytest
from app.main import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (0, 3, [0, 0, 0]),
        (2, 5, [0, 0, 0, 1, 1]),
    ]
)
def test_split_integer_standard_cases(
        value: int, number_of_parts: int, expected: list[int])\
        -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected
    assert sum(result) == value
    assert len(result) == number_of_parts
    assert max(result) - min(result) <= 1
    assert result == sorted(result)


def test_should_return_array_of_ones_when_value_equals_number_of_parts() \
        -> None:
    result = split_integer(5, 5)
    assert result == [1, 1, 1, 1, 1]


def test_result_should_be_sorted_ascending() -> None:
    result = split_integer(11, 3)
    assert result == sorted(result)


def test_difference_between_max_and_min_should_be_less_or_equal_to_one() \
        -> None:
    result = split_integer(35, 8)
    assert max(result) - min(result) <= 1
