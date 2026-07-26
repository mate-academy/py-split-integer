import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "values,numbers_of_parts,expected_result",
        [
            (36, 6, [6, 6, 6, 6, 6, 6]),
            (8, 1, [8]),
            (33, 5, [6, 6, 7, 7, 7]),
            (5, 8, [0, 0, 0, 1, 1, 1, 1, 1]),
        ]
    )
    def test_split_integer(
            self,
            values: int,
            numbers_of_parts: int,
            expected_result: list,
    ) -> None:
        assert split_integer(values, numbers_of_parts) == expected_result

    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        result = split_integer(32, 6)
        assert sum(result) == 32
