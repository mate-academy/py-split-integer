import pytest
from app.split_integer import split_integer


def test_should_return_zeros_when_value_is_zero() -> None:
    result = split_integer(0, 3)
    assert result == [0, 0, 0]


def test_should_handle_odd_values_splitting_even_parts() -> None:
    result = split_integer(7, 2)
    assert sum(result) == 7
    assert len(result) == 2
    assert result == [3, 4]


def test_should_handle_single_part_split() -> None:
    result = split_integer(10, 1)
    assert sum(result) == 10
    assert len(result) == 1
    assert result == [10]


def test_should_handle_large_numbers_correctly() -> None:
    result = split_integer(1000, 3)
    assert sum(result) == 1000
    assert len(result) == 3
    assert result == sorted(result)


def test_should_raise_when_number_of_parts_is_zero() -> None:
    with pytest.raises(ValueError):
        split_integer(10, 0)


def test_should_raise_when_number_of_parts_is_negative() -> None:
    with pytest.raises(ValueError):
        split_integer(10, -2)


def test_should_raise_when_value_is_negative() -> None:
    with pytest.raises(ValueError):
        split_integer(-10, 2)
