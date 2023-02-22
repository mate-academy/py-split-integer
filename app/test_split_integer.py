import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "number,parts,result",
    [
        pytest.param(9, 3, [3, 3, 3], id="equal parts expected if possible"),
        pytest.param(5, 1, [5], id="same value expected when part = 1"),
        pytest.param(11, 3, [3, 4, 4], id="sorted list expected"),
        pytest.param(2, 3, [0, 1, 1], id="should add zeros if parts > value"),
    ]
)
def test_split_int(number: int, parts: int, result: list) -> None:
    assert split_integer(number, parts) == result, (
        f"expected {result} when number is {number} and parts is {parts}")
