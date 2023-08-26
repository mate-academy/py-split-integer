from app.split_integer import split_integer

import pytest


@pytest.mark.parametrize(
    "initial_parts, except_result",
    [
        pytest.param(
            [1, 1], [1], id="sum of the parts should be equal to value"
        ),
        pytest.param(
            [6, 2],
            [3, 3],
            id="should split into equal parts when value divisible by parts",
        ),
        pytest.param(
            [8, 0],
            [],
            id="should return part equals to value when split into one part",
        ),
        pytest.param(
            [17, 4],
            [4, 4, 4, 5],
            id="parts should be sorted when they are not equal",
        ),
        pytest.param(
            [2, 4],
            [0, 0, 1, 1],
            id="should add zeros when value is less than number of parts",
        ),
    ],
)
def test_modify_parts_correctly(
    initial_parts: list, except_result: int
) -> None:
    assert split_integer(initial_parts[0], initial_parts[1]) == except_result


@pytest.mark.parametrize(
    "initial_parts, except_result",
    [
        pytest.param(
            "abs", TypeError, id="should raise error when parts is not int"
        ),
        pytest.param(
            [3.2, 1.1],
            TypeError,
            id="should raise error when parts is not int",
        ),
    ],
)
def test_should_raise_error(initial_parts: any, except_result: any) -> None:
    with pytest.raises(except_result):
        split_integer(initial_parts[0], initial_parts[1])
