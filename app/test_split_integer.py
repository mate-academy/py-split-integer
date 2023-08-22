import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            pytest.param(
                25,
                5,
                [5, 5, 5, 5, 5],
                id=(
                    "should split into equal parts"
                    "when value divisible by parts"
                )
            ),
            pytest.param(
                8,
                1,
                [8],
                id=(
                    "should return part equals to value when"
                    "split into one part"
                )
            ),
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                3,
                6,
                [0, 0, 0, 1, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_should_return_correct_values(
            self,
            value: int,
            number_of_parts: int,
            expected_result: int | list[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == expected_result

    def test_sum_of_result_should_be_equal_to_value(self) -> None:
        assert sum(split_integer(100, 4)) == 100
