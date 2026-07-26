import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "split_value,split_number_of_parts,split_parts",
        [
            pytest.param(
                6,
                2,
                [3, 3],
                id="sum of the parts should be equal to value"
            ),
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id=("should split into equal parts "
                    "when value divisible by parts")
            ),
            pytest.param(
                17,
                0,
                [],
                id=("should return part equals to "
                    "value when split into one part")
            ),
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                2,
                6,
                [0, 0, 0, 0, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_result_corrected(
            self,
            split_value: int,
            split_number_of_parts: int,
            split_parts: list[int]
    ) -> None:

        assert split_integer(split_value, split_number_of_parts) == split_parts
