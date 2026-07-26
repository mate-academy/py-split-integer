import pytest
from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, expected_result",
        [
            pytest.param(
                10,
                4,
                [2, 2, 3, 3],
                id="sum of the parts should be equal to value",
            ),
            pytest.param(
                10,
                5,
                [2] * 5,
                id=(
                    "should split into equal parts "
                    "when value divisible by parts"
                ),
            ),
            pytest.param(
                10,
                1,
                [10],
                id=(
                    "should return part equals to "
                    "value when split into one part"
                ),
            ),
            pytest.param(
                10,
                4,
                [2, 2, 3, 3],
                id="parts should be sorted when they are not equal",
            ),
            pytest.param(
                10,
                11,
                [0] + [1] * 10,
                id="should add zeros when value is less than number of parts",
            ),
        ],
    )
    def test_split_integer(
        self, value: int, number_of_parts: int, expected_result: list[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == expected_result
