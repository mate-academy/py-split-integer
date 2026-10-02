import pytest

from app import split_integer


@pytest.mark.parametrize(
    "value,parts,result",
    [
        pytest.param(
            8,
            1,
            8,
            id="sum of the parts should be equal to value",
        ),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    parts: int,
    result: int,
) -> None:
    assert sum(split_integer.split_integer(value, parts)) == result


@pytest.mark.parametrize(
    "value,parts,result",
    [
        pytest.param(
            6,
            2,
            [3, 3],
            id="split into equal parts when value divisible by parts",
        ),
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    parts: int,
    result: list[int],
) -> None:
    assert split_integer.split_integer(value, parts) == result


@pytest.mark.parametrize(
    "value,parts,result",
    [
        pytest.param(
            8,
            1,
            [8],
            id="_return_part_equals_to_value_when_split_into_one_part",
        ),
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    parts: int,
    result: list[int],
) -> None:
    assert split_integer.split_integer(value, parts) == result


@pytest.mark.parametrize(
    "value,parts,result",
    [
        pytest.param(
            17,
            4,
            [4, 4, 4, 5],
            id="test parts should be sorted when they are not equal",
        ),
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    parts: int,
    result: list[int],
) -> None:
    assert split_integer.split_integer(value, parts) == result


@pytest.mark.parametrize(
    "value,parts,result",
    [
        pytest.param(
            3,
            5,
            [0, 0, 1, 1, 1],
            id="test parts should be sorted when they are not equal",
        ),
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    parts: int,
    result: list[int],
) -> None:
    assert split_integer.split_integer(value, parts) == result
