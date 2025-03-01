import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize("value,parts", [
    (8, 1),
    (6, 2),
    (17, 4),
    (32, 6),
    (5, 8),
    (1, 3)
])
class TestSplitInteger:
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            value: int,
            parts: int) -> None:
        result = split_integer(value, parts)

        assert sum(result) == value

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self,
            value: int,
            parts: int) -> None:
        if value % parts != 0:
            pytest.skip("Only when value divisible by parts")
            return
        result = split_integer(value, parts)
        assert result == [value // parts] * parts

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self,
            value: int,
            parts: int) -> None:
        if parts != 1:
            pytest.skip("Only when value split into one part")
            return

        result = split_integer(value, parts)
        assert result == [value]

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self,
            value: int,
            parts: int) -> None:
        if (value % parts) == 0:
            pytest.skip("Only when parts are not equal")
            return
        result = split_integer(value, parts)
        assert result == sorted(result)

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self,
            value: int,
            parts: int) -> None:
        if value >= parts:
            pytest.skip("Only when value is less than number of parts")
            return
        result = split_integer(value, parts)
        assert result == ([0] * (parts - value)) + [1] * value
