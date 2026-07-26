from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value,parts_number,expected", [
        pytest.param(
            8,
            1,
            [8],
            id="Sum of the parts should be equal to value"
        ),
        pytest.param(
            8,
            2,
            [4, 4],
            id="Should split into equal parts, when value divisible by parts"
        ),
        pytest.param(
            9,
            1,
            [9],
            id="Should return part equals to value, when split into one part"
        ),
        pytest.param(
            17,
            4,
            [4, 4, 4, 5],
            id="Parts should be sorted when they are not equal"
        ),
        pytest.param(
            2,
            4,
            [0, 0, 1, 1],
            id="Should add zeros when value is less than number of parts"
        )
    ]
)
def test_split_integer(value: int, parts_number: int, expected: list) -> None:
    assert split_integer(value, parts_number) == expected
