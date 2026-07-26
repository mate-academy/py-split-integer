import pytest

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 39, 6
    result = split_integer(value, parts)
    assert all(isinstance(number, int) for number in result)
    assert max(result) - min(result) <= 1
    assert sum(result) == value
    assert len(result) == parts
    assert result == sorted(result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 15, 3
    result = split_integer(value, parts)
    assert split_integer(value, parts) == [5, 5, 5]
    assert all(isinstance(number, int) for number in result)
    assert max(result) - min(result) <= 1
    assert len(result) == parts
    assert result == sorted(result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 8, 1
    result = split_integer(value, parts)
    assert split_integer(value, parts) == [8]
    assert all(isinstance(number, int) for number in result)
    assert max(result) - min(result) <= 1
    assert len(result) == parts
    assert result == sorted(result)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 321, 7
    result = split_integer(value, parts)
    assert all(isinstance(number, int) for number in result)
    assert max(result) - min(result) <= 1
    assert len(result) == parts
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 5, 6
    result = split_integer(value, parts)
    assert result == [0, 1, 1, 1, 1, 1]
    assert all(isinstance(number, int) for number in result)
    assert max(result) - min(result) <= 1
    assert len(result) == parts
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, parts, result",
    [
        pytest.param(6, 2, [3, 3], id="6, 2"),
        pytest.param(17, 4, [4, 4, 4, 5], id="17, 4"),
        pytest.param(32, 6, [5, 5, 5, 5, 6, 6], id="32, 6")
    ]
)
def test_values_split_integer(value: int, parts: int, result: list) -> None:
    test = split_integer(value, parts)
    assert test == result
    assert all(isinstance(number, int) for number in test)
    assert max(test) - min(test) <= 1
    assert len(test) == parts
    assert sum(test) == value
