import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, parts",
    [
        pytest.param(
            6,
            6,
            [1, 1, 1, 1, 1, 1],
            id="test sum of the parts "
               "should be equal to value"
        ),
        pytest.param(
            6,
            2,
            [3, 3],
            id="test should split into equal "
               "parts when value divisible by parts"
        ),
        pytest.param(
            8,
            1,
            [8],
            id="test should return part equals "
               "to value when split into one part"
        ),
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="test parts should be sorted "
               "when they are not equal"
        ),
        pytest.param(
            3,
            6,
            [0, 0, 0, 1, 1, 1],
            id="test should add zeros when "
               "value is less than number of parts"
        ),
    ]
)
def test_split_integer_should_function_with_different_params(
        value: int,
        number_of_parts: int,
        parts: list
) -> None:
    assert split_integer(value, number_of_parts) == parts
