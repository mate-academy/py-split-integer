import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, expected_result",
        [
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id=("should split into equal parts when"
                    " value divisible by parts")
            ),
            pytest.param(
                8,
                1,
                [8],
                id=("should return part equals to value when"
                    " split into one part")
            ),
            pytest.param(
                0,
                4,
                [0, 0, 0, 0],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_check_right_values(
            self,
            value: int,
            number_of_parts: int,
            expected_result: list
    ) -> None:
        assert split_integer(value, number_of_parts) == expected_result


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == sum([5, 5, 5, 5, 6, 6])


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(26, 4)) == [6, 6, 7, 7]
