import pytest
from app.split_integer import split_integer


def test_split_integer_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_uneven_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_more_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_explicit_remainder_cases() -> None:

    assert split_integer(5, 3) == [1, 2, 2]
    assert split_integer(7, 4) == [1, 2, 2, 2]

    assert split_integer(9, 4) == [2, 2, 2, 3]

    assert split_integer(6, 3) == [2, 2, 2]

    assert split_integer(6, 5) == [1, 1, 1, 1, 2]
    assert split_integer(3, 2) == [1, 2]


@pytest.mark.parametrize("value, parts", [
    (1, 1), (2, 2), (10, 3), (10, 4), (100, 7), (17, 4), (32, 6)
])
def test_properties_and_pattern(value: int, parts: int) -> None:
    result = split_integer(value, parts)
    assert isinstance(result, list)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    base = value // parts
    rem = value % parts
    expected = [base] * (parts - rem) + [base + 1] * rem
    assert result == expected
