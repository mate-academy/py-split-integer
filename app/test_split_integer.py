import pytest
import app.split_integer as split_integer


@pytest.mark.parametrize(
    "value, parts",
    [
        (17, 4),
        (35, 8),
        (5, 3),
        (2, 3),
        (1, 3),
        (6, 2),
        (20, 5),
    ],
)
def test_basic_rules(value: int, parts: int) -> None:
    result = split_integer.split_integer(value, parts)

    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_equal_distribution_when_divisible() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]
    assert split_integer.split_integer(20, 5) == [4, 4, 4, 4, 4]
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_correct_distribution_of_remainder() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer.split_integer(5, 3) == [1, 2, 2]


def test_value_less_than_parts() -> None:
    assert split_integer.split_integer(2, 3) == [0, 1, 1]
    assert split_integer.split_integer(1, 3) == [0, 0, 1]
