import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    (
        pytest.param(
            8,
            1,
            [8],
            id="should return part equals to value when split into one part",
        ),
        pytest.param(
            17,
            4,
            [4, 4, 4, 5],
            id="parts should be sorted when they are not equal",
        ),
        pytest.param(
            5,
            6,
            [0, 1, 1, 1, 1, 1],
            id="should add zeros when value is less than number of parts",
        ),
        pytest.param(
            36,
            6,
            [6, 6, 6, 6, 6, 6],
            id="should split into equal parts when value divisible by parts",
        ),
    ),
)
def test_correct_work_of_split_integer(
    value: int, number_of_parts: int, result_list: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == result_list
