import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        assert sum(split_integer(20, 4)) == 20, ("sum of the parts should be "
                                                 "equal to the original value")

    @pytest.mark.parametrize(
        "value, number_of_parts, result",
        [
            pytest.param(
                20,
                5,
                [4, 4, 4, 4, 4],
                id=("should split into equal parts "
                    "when value divisible by parts")
            ),
            pytest.param(
                5,
                1,
                [5],
                id=("should return part equals to value "
                    "when split into one part")
            ),
            pytest.param(
                30,
                4,
                [7, 7, 8, 8],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                5,
                8,
                [0, 0, 0, 1, 1, 1, 1, 1],
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
