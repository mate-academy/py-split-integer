import pytest
from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,result",
        [
            pytest.param(
                10, 2,
                [5, 5],
                id="test sum of the parts should be equal to value"
            ),
            pytest.param(
                9, 3,
                [3, 3, 3],
                id=("test should split into equal "
                    "parts when value divisible by parts")
            ),
            pytest.param(
                8, 1,
                [8],
                id=("test should return part equals "
                    "to value when split into one part")
            ),
            pytest.param(
                30, 4,
                [7, 7, 8, 8],
                id="test parts should be sorted when they are not equal"
            ),
            pytest.param(
                1, 3,
                [0, 0, 1],
                id=("test should add zeros when "
                    "value is less than number of parts")
            )
        ]
    )
    def test_split_integer(
            self,
            value: int,
            number_of_parts: int,
            result: list[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == result
