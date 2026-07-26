import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "initial_integer, parts_for_split, expected_result",
        [
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="sum of the parts should be equal to value"
            ),

            pytest.param(
                16,
                4,
                [4, 4, 4, 4],
                id="should split into equal parts "
                   "when value divisible by parts"
            ),

            pytest.param(
                8,
                1,
                [8],
                id="should return part equals to "
                   "value when split into one part"
            ),

            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id="stest parts should be sorted when they are not equal"
            ),

            pytest.param(
                3,
                5,
                [0, 0, 1, 1, 1],
                id="should add zeros when value is less than number of parts"
            )

        ]
    )
    def test_spliting_integer_correctly(
            self,
            initial_integer: int,
            parts_for_split: int,
            expected_result: list
    ) -> None:
        assert \
            split_integer(initial_integer, parts_for_split) == expected_result
