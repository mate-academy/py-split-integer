import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected_result", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6])
])
def test_split_integer(
        value: int,
        number_of_parts: int,
        expected_result: int
) -> None:
    """
    Test for split_integer function.
    """
    assert split_integer(value, number_of_parts) == expected_result
