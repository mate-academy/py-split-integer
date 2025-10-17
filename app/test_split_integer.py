import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_should_match_examples_from_specification(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 3),
        (3, 5),
        (20, 4),
        (21, 4),
    ],
)
def test_general_behavior_of_split_integer(
    value: int,
    number_of_parts: int,
) -> None:

    result = split_integer(value, number_of_parts)

    assert sum(result) == value

    assert len(result) == number_of_parts

    assert all(isinstance(x, int) for x in result)

    assert result == sorted(result)

    assert max(result) - min(result) <= 1
