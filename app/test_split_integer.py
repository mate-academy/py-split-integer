import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value,expected_result",
    [
        (8, [4, 4]),
        (6, [3, 3]),
        (16, [8, 8]),
        (32, [16, 16])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        expected_result: list
) -> None:
    assert split_integer(value, 2) == expected_result


@pytest.mark.parametrize("value", [8, 6, 17, 32])
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int
) -> None:
    assert split_integer(value, 1) == [value]


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    result_list = split_integer(value, number_of_parts)
    sorted_list = sorted(result_list)
    assert result_list == sorted_list


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2)[0] == 0
