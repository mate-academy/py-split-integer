import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
class TestSplitInteger:
    def setup_method(self, method: str) -> None:
        self.result = None

    def calculate_result(self, value: int, number_of_parts: int) -> None:
        self.result = split_integer(value, number_of_parts)

    def test_sum_of_the_parts_should_be_equal_to_value(
        self, value: int, number_of_parts: int
    ) -> None:
        self.calculate_result(value, number_of_parts)
        assert sum(self.result) == value, (
            f"Expected sum of parts to be {value}, but got {sum(self.result)}"
        )

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        self, value: int, number_of_parts: int
    ) -> None:
        self.calculate_result(value, number_of_parts)
        if value % number_of_parts == 0:
            expected_part = value // number_of_parts
            for part in self.result:
                assert part == expected_part, (
                    f"Expected {expected_part}, but got {part}"
                )

    def test_should_return_part_equals_to_value_when_split_into_one_part(
        self, value: int, number_of_parts: int
    ) -> None:
        self.calculate_result(value, number_of_parts)
        if number_of_parts == 1:
            assert self.result == [value], (
                f"Expected result to be [{value}], but got {self.result}"
            )

    def test_parts_should_be_sorted_when_they_are_not_equal(
        self, value: int, number_of_parts: int
    ) -> None:
        self.calculate_result(value, number_of_parts)
        sorted_result = sorted(self.result)
        assert self.result == sorted_result, (
            f"Expected result must be sorted {sorted_result}, "
            f"but got {self.result}"
        )

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        self, value: int, number_of_parts: int
    ) -> None:
        self.calculate_result(value, number_of_parts)
        if value < number_of_parts:
            assert all(x >= 0 for x in self.result), (
                f"Expected non-negative parts, but got {self.result}"
            )
