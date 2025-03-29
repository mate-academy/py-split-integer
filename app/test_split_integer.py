import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,result",
        [
            pytest.param(
                125,
                5,
                [25, 25, 25, 25, 25],
                id=("should split into equal parts "
                    "when value divisible by parts")
            ),
            pytest.param(
                22,
                1,
                [22],
                id=("should return part equals"
                    "to value when split into one part")
            ),
            pytest.param(
                19,
                7,
                [2, 2, 3, 3, 3, 3, 3],
                id="should be sorted, when they are not equal"
            ),
            pytest.param(
                6,
                12,
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_should_return_correct_values(
            self,
            value: int,
            number_of_parts: int,
            result: list[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == result


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(2, 2)) == 2
