import pytest
from app.split_integer import split_integer


def test_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_unequal_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_many_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_on_different_parts() -> None:
    parts = split_integer(10, 3)
    assert len(parts) == 3
    assert sum(parts) == 10
    assert max(parts) - min(parts) <= 1


def test_only_last_number_is_incremented() -> None:
    parts = split_integer(5, 3)
    assert parts == [1, 2, 2]


def test_split_on_incorrect_parts() -> None:
    with pytest.raises(ZeroDivisionError):
        split_integer(10, 0)
