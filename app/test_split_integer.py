import pytest
from app import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, parts",
        [(3, 3), (17, 4), (9, 3), (2, 4), (100, 9)],
    )
    def test_sum_of_the_parts_should_be_equal_to_value(
        self, value: int, parts: int
    ) -> None:
        """Ensure the sum of parts equals the original value."""
        result = split_integer.split_integer(value, parts)
        assert sum(result) == value, f"Mismatch for val={value}, part={parts}"

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self) -> None:
        """Check equal split when value divisible by number of parts."""
        result = split_integer.split_integer(6, 2)
        assert result == [3, 3], f"Expected [3, 3], got {result}"

    @pytest.mark.parametrize("value, expected", [(8, [8]), (3, [3])])
    def test_should_return_part_equals_to_value_when_split_into_one_part(
        self, value: int, expected: list[int]
    ) -> None:
        """Check single part case."""
        result = split_integer.split_integer(value, 1)
        assert result == expected, f"Expected {expected}, got {result}"

    @pytest.mark.parametrize(
        "value, parts, expected",
        [
            (17, 4, [4, 4, 4, 5]),
            (32, 6, [5, 5, 5, 5, 6, 6]),
        ],
    )
    def test_parts_should_be_sorted_when_they_are_not_equal(
        self, value: int, parts: int, expected: list[int]
    ) -> None:
        """Ensure parts are sorted and match expected uneven splits."""
        result = split_integer.split_integer(value, parts)
        assert result == expected, f"Expected {expected}, got {result}"

    @pytest.mark.parametrize(
        "value, parts, expected",
        [(2, 4, [0, 0, 1, 1]), (1, 3, [0, 0, 1]), (3, 5, [0, 0, 1, 1, 1])],
    )
    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        self, value: int, parts: int, expected: list[int]
    ) -> None:
        """Add zeros when value < parts."""
        result = split_integer.split_integer(value, parts)
        assert result == expected, f"Expected {expected}, got {result}"

    @pytest.mark.parametrize(
        "value, parts", [(17, 4), (10, 3), (2, 4), (100, 9), (7, 3)]
    )
    def test_difference_between_parts_should_be_at_most_one(
        self, value: int, parts: int
    ) -> None:
        """Ensure all parts differ by at most one."""
        result = split_integer.split_integer(value, parts)
        max_diff = max(result) - min(result)
        assert max_diff <= 1, (
            f"Parts differ by more than 1 for value={value}, parts={parts}"
        )

    @pytest.mark.parametrize("value, parts", [(17, 4), (2, 4), (9, 3), (1, 5)])
    def test_should_return_correct_number_of_parts(
        self, value: int, parts: int
    ) -> None:
        """Ensure correct number of parts returned."""
        result = split_integer.split_integer(value, parts)
        assert len(result) == parts, (
            f"Expected {parts} parts, got {len(result)}"
        )

    @pytest.mark.parametrize("value, parts",
                             [(10, 3), (11, 4), (17, 4), (2, 4)]
                             )
    def test_result_should_not_depend_on_order_of_distribution(
        self, value: int, parts: int
    ) -> None:
        """Remainder distribution should not affect sorted result."""
        result = split_integer.split_integer(value, parts)
        expected = sorted(result)
        assert result == expected, f"Order inconsistency for value={value}"
