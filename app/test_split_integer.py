import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        pytest.param(6, 2, [3, 3],
                     id=" if value % parts is zero - parts should be equal"),
        pytest.param(8, 1, [8],
                     id="should return list with value when parts equal one"),
        pytest.param(32, 6, [5, 5, 5, 5, 6, 6],
                     id="returned list should be sorted in ascending order"),
        pytest.param(6, 7, [0, 1, 1, 1, 1, 1, 1],
                     id="should add zeros to value when parts > value")
    ]
)
def test_split_integer(value: int, parts: int, expected: list[int]) -> None:
    assert split_integer(value, parts) == expected
