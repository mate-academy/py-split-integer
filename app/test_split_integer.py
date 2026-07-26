import pytest
from app.split_integer import split_integer


def test_single_part_returns_whole_value() -> None:
    """Test that a single part returns the entire value."""
    assert split_integer(8, 1) == [8]


def test_even_split() -> None:
    """Test that an even division splits correctly."""
    assert split_integer(6, 2) == [3, 3]


def test_uneven_split_small_remainder() -> None:
    """Test uneven split with small remainder distributes correctly."""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_large_uneven_split() -> None:
    """Test uneven split with multiple larger elements."""
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_difference_between_min_and_max_is_one_or_less() -> None:
    """Ensure that the difference between min and max does not exceed 1."""
    result = split_integer(20, 6)
    assert max(result) - min(result) <= 1


def test_result_has_correct_number_of_parts() -> None:
    """Ensure that the result has exactly number_of_parts elements."""
    number_of_parts = 5
    result = split_integer(14, number_of_parts)
    assert len(result) == number_of_parts


def test_sum_of_parts_equals_original_value() -> None:
    """Ensure that the sum of all parts equals the input value."""
    value = 25
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_result_is_sorted_ascending() -> None:
    """Ensure that the resulting list is sorted in ascending order."""
    result = split_integer(19, 5)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (5, 2, [2, 3]),
        (10, 3, [3, 3, 4]),
        (11, 3, [3, 4, 4]),
        (9, 4, [2, 2, 2, 3]),
    ],
)
def test_parametrized_cases(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    """Test multiple parameterized input-output pairs."""
    assert split_integer(value, number_of_parts) == expected
