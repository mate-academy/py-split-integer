from app.split_integer import split_integer
import pytest

@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        (6, 2, [3, 3]),
        (100, 4, [25 for _ in range(4)])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int,
    result_list: list
) -> None:
    assert split_integer(value, number_of_parts) == result_list


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        (7, 1, [7])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int,
    result_list: list
) -> None:
    assert  split_integer(value, number_of_parts) == result_list


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value,
        number_of_parts
) -> None:
    result = split_integer(value, number_of_parts)
    assert result[0] <= result[-1]

@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        (7, 8, [0 for _ in range(8 - 7)] + split_integer(7, 7)),
        (7, 10, [0 for _ in range(10 - 7)] + split_integer(7, 7)),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    assert split_integer(value, number_of_parts) == result_list
