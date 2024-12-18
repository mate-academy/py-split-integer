import pytest
from app.split_integer import split_integer


class TestSplitIntegerFunction:
    @pytest.mark.parametrize(
        "entered_numbers,expected_result",
        [
            pytest.param(
                (8, 1),
                [8],
                id="sum of the parts should be equal to value"
            ),
            pytest.param(
                (32, 6),
                [5, 5, 5, 5, 6, 6],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                (1, 2),
                [0, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_general_function_test(
        self,
        entered_numbers: tuple,
        expected_result: list
    ) -> None:
        result = split_integer(*entered_numbers)
        assert result == expected_result


def test_should_return_valid_parts_when_split_into_multiple_parts() -> None:
    result = split_integer(17, 4)
    assert len(result) == 4
    assert sum(result) == 17
    assert max(result) - min(result) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert len(result) == 2 and sum(result) == 6
