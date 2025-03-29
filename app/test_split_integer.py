import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(
            6,
            2,
            [3, 3],
            id="should split into equal parts when value divisible "
               "by parts"
        ),
        pytest.param(
            6,
            2,
            [3, 3],
            id="should return part equals to value when split "
               "into one part"
        ),
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="parts should be sorted when they are not equal"
        ),
        pytest.param(
            1,
            4,
            [0, 0, 0, 1],
            id="should add zeros when value is less than "
               "number of parts"
        ),
    ]
)
def test_split_integer(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected
