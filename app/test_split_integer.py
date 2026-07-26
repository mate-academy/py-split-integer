import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(
            8,
            2,
            [4, 4],
            id="should split into equal parts when value divisible by parts"
        ),
        pytest.param(
            8,
            1,
            [8],
            id="should return part equals to value when split into one part"
        ),
        pytest.param(
            9,
            2,
            [4, 5],
            id="parts should be sorted when they are not equal"
        ),
        pytest.param(
            3,
            5,
            [0, 0, 1, 1, 1],
            id="should add zeros when value is less than number of parts"
        ),
    ]
)
def test_split_integer_correct_work(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert (
        split_integer(value, number_of_parts) == result
    ), (f"The number {value} when divided into "
        f"{number_of_parts} parts must be equal to {result}")
