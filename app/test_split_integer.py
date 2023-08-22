import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, expected_result",
        [
            pytest.param(
                6,
                2,
                [3, 3],
                id="test should split into equal parts "
                "when value divisible by parts",
            ),
            pytest.param(
                8,
                1,
                [8],
                id="test should return part equals to value "
                "when split into one part",
            ),
            pytest.param(
                4,
                6,
                [0, 0, 1, 1, 1, 1],
                id="test should add zeros "
                "when value is less than number of parts",
            ),
        ],
    )
    def test_split_integer_correctly(
        self, value: int, number_of_parts: int, expected_result: list
    ) -> None:
        result = split_integer(value, number_of_parts)

        assert result == expected_result

    def test_parts_should_be_sorted_when_they_are_not_equal(self):
        value = 17
        number_of_parts = 4
        result = split_integer(value, number_of_parts)

        assert sorted(result) == result

    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        value = 17
        number_of_parts = 4
        result = split_integer(value, number_of_parts)

        assert sum(result) == value
