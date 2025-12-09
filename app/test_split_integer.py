import pytest
from app import split_integer as s_i


class TestSplitInteger:

    @pytest.mark.parametrize(
        "value, number_of_parts, expected",
        [
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id="sum of the parts should be equal to value"
            ),
            pytest.param(
                6,
                2,
                [3, 3],
                id="test should split into"
                   " equal parts when value divisible by parts"
            ),
            pytest.param(
                8,
                1,
                [8],
                id="test should return part "
                   "equals to value when split into one part"
            ),
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="test parts should be sorted "
                   "when they are not equal"
            ),
            pytest.param(
                5,
                6,
                [0, 1, 1, 1, 1, 1],
                id="test should add zeros when "
                   "value is less than number of parts"
            )
        ]
    )
    def test_split_integer(
            self,
            value: int,
            number_of_parts: int,
            expected: list
    ) -> None:
        assert s_i.split_integer(value, number_of_parts) == expected
