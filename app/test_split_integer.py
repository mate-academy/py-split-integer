import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value_for_check,number_of_parts_for_check,excepted_result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value_for_check: int,
        number_of_parts_for_check: int,
        excepted_result: list) -> None:
    result = split_integer(value_for_check, number_of_parts_for_check)
    assert result == excepted_result


@pytest.mark.parametrize(
    "value_for_check,number_of_parts_for_check,excepted_result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (16, 4, [4, 4, 4, 4]),
        (30, 6, [5, 5, 5, 5, 5, 5]),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value_for_check: int,
        number_of_parts_for_check: int,
        excepted_result: list) -> None:
    result = split_integer(value_for_check, number_of_parts_for_check)
    assert result == excepted_result


@pytest.mark.parametrize(
    "value_for_check,number_of_parts_for_check,excepted_result",
    [
        (8, 1, [8]),
        (6, 1, [6]),
        (16, 1, [16]),
        (30, 1, [30])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value_for_check: int,
        number_of_parts_for_check: int,
        excepted_result: list) -> None:
    result = split_integer(value_for_check, number_of_parts_for_check)
    assert result == excepted_result


@pytest.mark.parametrize(
    "value_for_check,number_of_parts_for_check",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value_for_check: int,
        number_of_parts_for_check: int) -> None:
    result = split_integer(value_for_check, number_of_parts_for_check)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value_for_check,number_of_parts_for_check",
    [
        (8, 214),
        (6, 30),
        (17, 123),
        (32, 2352)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value_for_check: int,
        number_of_parts_for_check: int) -> None:
    result = split_integer(value_for_check, number_of_parts_for_check)
    assert result.count(0) == number_of_parts_for_check - value_for_check
