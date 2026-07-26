from app.split_integer import split_integer

import pytest


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int, result: list[int]
) -> None:
    output = split_integer(value, number_of_parts)
    assert sum(output) == value, f"Expected sum {value}, got {sum(output)}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (10, 5, [2] * 5),
        (9, 3, [3] * 3),
        (100, 10, [10] * 10),
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int, result: list[int]
) -> None:
    output = split_integer(value, number_of_parts)
    assert len(set(output)) == 1, (
        f"Parts should be equal, got different: {set(output)}"
    )


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (7, 1, [7]),
        (52, 1, [52]),
        (0, 1, [0]),
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, number_of_parts: int, result: list[int]
) -> None:
    output = split_integer(value, number_of_parts)
    assert output == result, f"Expected single part {result}, got {output}"
    assert len(output) == 1, f"Expected one part, got {len(output)}"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (10, 3),
        (17, 4),
        (31, 6),
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:
    output = split_integer(value, number_of_parts)
    assert output == sorted(output), f"Parts should be sorted, got {output}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (2, 5, [0, 0, 0, 1, 1]),
        (0, 3, [0, 0, 0]),
        (1, 4, [0, 0, 0, 1]),
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, number_of_parts: int, result: list[int]
) -> None:
    output = split_integer(value, number_of_parts)
    assert output == result, f"Expected {result}, got {output}"
