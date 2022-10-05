import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, return_result",
    [
        pytest.param(
            6,
            2,
            [3, 3],
            id=("should split into equal parts "
                "when value is divisible by parts")
        ),
        pytest.param(
            8,
            1,
            [8],
            id=("should return part equals to "
                "value when slitting into one part")
        ),
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="parts should be sorted when they are not equal"
        ),
        pytest.param(
            2,
            5,
            [0, 0, 0, 1, 1],
            id="should add zeros when value is less than number of parts"
        )
    ]
)
def test_correct_values(value, number_of_parts, return_result):
    assert split_integer(value, number_of_parts) == return_result


@pytest.mark.parametrize(
    "value, number_of_parts, return_result",
    [
        pytest.param(
            8,
            2,
            8,
            id="sum of the parts should be equal to value"
        )
    ]
)
def test_correct_values_for_sum(value, number_of_parts, return_result):
    assert sum(split_integer(value, number_of_parts)) == return_result
