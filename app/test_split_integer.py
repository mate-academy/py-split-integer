import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected_parts",
    [
        pytest.param(
            18,
            6,
            [3, 3, 3, 3, 3, 3],
            id="sum of the parts should be equal to value"
        ),
        pytest.param(
            6,
            2,
            [3, 3],
            id="should split into equal parts when value divisible by parts"
        ),
        pytest.param(
            8,
            1,
            [8],
            id="should return part equals to value when split into one part"
        ),
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="parts should be sorted when they are not equal"
        ),
        pytest.param(
            4,
            6,
            [0, 0, 1, 1, 1, 1],
            id="should add zeros when value is less than number of parts"
        ),
    ]
)
def test_function_split_integer_with_different_params(
        value: int,
        number_of_parts: int,
        expected_parts: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected_parts
