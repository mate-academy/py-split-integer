import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected_result", [
    (8, 1, [8]),           # Single part
    (6, 2, [3, 3]),        # Two equal parts
    (17, 4, [4, 4, 4, 5]), # Unequal parts, difference <= 1
    (32, 6, [5, 5, 5, 5, 6, 6])  # Six parts
])
def test_split_integer(value, number_of_parts, expected_result):
    """
    Test for split_integer function.
    """
    assert split_integer(value, number_of_parts) == expected_result
