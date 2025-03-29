import pytest


from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "initial_number,parts_to_divide,expected_result",
        [
            pytest.param(
                16,
                4,
                [4, 4, 4, 4],
                id=("should split into equal parts"
                    " when value divisible by parts")
            ),
            pytest.param(
                4,
                1,
                [4],
                id=("should return part equals"
                    " to value when split into one part")
            ),
            pytest.param(
                33,
                6,
                [5, 5, 5, 6, 6, 6],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                3,
                5,
                [0, 0, 1, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_split_integer_output(
        self,
        initial_number: int,
        parts_to_divide: int,
        expected_result: list[int]
    ) -> None:
        split_integer_result = split_integer(initial_number, parts_to_divide)
        assert split_integer_result == expected_result
