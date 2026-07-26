import pytest

from app import split_integer


class TestSplitInteger:
    def _check_all_rules(self, result: list, value: int, parts: int) -> None:
        assert len(result) == parts
        assert sum(result) == value
        assert result == sorted(result)
        assert result[-1] - result[0] <= 1

    @pytest.mark.parametrize(
        "value, parts",
        [(8, 1), (6, 2), (17, 4), (32, 6), (2, 3), (1, 5), (10, 10)],
    )
    def test_split_integer_logic_comprehensive(
        self, value: int, parts: int
    ) -> None:
        self._check_all_rules(
            split_integer.split_integer(value, parts), value, parts
        )

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        self,
    ) -> None:
        value, parts = 8, 2
        result = split_integer.split_integer(value, parts)
        self._check_all_rules(result, value, parts)
        assert result == [4, 4]

    def test_should_return_part_equals_to_value_when_split_into_one_part(
        self,
    ) -> None:
        value, parts = 10, 1
        result = split_integer.split_integer(value, parts)
        self._check_all_rules(result, value, parts)
        assert result == [10]

    def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
        value, parts = 32, 6
        result = split_integer.split_integer(value, parts)
        self._check_all_rules(result, value, parts)
        assert result == [5, 5, 5, 5, 6, 6]

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        self,
    ) -> None:
        value, parts = 2, 4
        result = split_integer.split_integer(value, parts)
        self._check_all_rules(result, value, parts)
        assert result == [0, 0, 1, 1]
