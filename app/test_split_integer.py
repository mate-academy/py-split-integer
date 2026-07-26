import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "initial_value,number_of_parts,result",
        [
            pytest.param(
                8,
                1,
                [8],
                id="should return part equals "
                   "to value when split into one part"
            ),
            pytest.param(
                6,
                2,
                [3, 3],
                id="should split into equal parts "
                   "when value divisible by parts"
            ),
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id="parts should be sorted "
                   "when they are not equal"
            ),
            pytest.param(
                2,
                5,
                [0, 0, 0, 1, 1],
                id="should add zeros when value "
                   "is less than number of parts"
            )
        ]
    )
    def test_split_integer(
            self,
            initial_value: int,
            number_of_parts: int,
            result: []
    ) -> None:
        actual_result = split_integer(initial_value, number_of_parts)
        assert actual_result == result, (
            f"Expected split of {initial_value} into "
            f"{number_of_parts} parts to be {result}, "
            f"but got {actual_result} instead."
        )
