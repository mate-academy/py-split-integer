import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, result",
        [
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="test sum of the parts should be equal to value"
            ),
            pytest.param(
                9,
                3,
                [3, 3, 3],
                id=("should split into equal parts "
                    "when value divisible by parts")
            ),
            pytest.param(
                6,
                1,
                [6],
                id=("should return part equals to value "
                    "when split into one part")
            ),
            pytest.param(
                19,
                4,
                [4, 5, 5, 5],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                2,
                4,
                [0, 0, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_split_integer_correctly(
        self,
        value: int,
        number_of_parts: int,
        result: list
    ) -> None:
        assert split_integer(value, number_of_parts) == result
