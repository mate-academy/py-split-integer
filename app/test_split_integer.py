import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (100, 20),
        (4759, 37)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (15, 3),
        (48, 6),
        (100, 20),
        (225, 5)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts) == [value // number_of_parts] * number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 1),
        (17, 1),
        (32, 1),
        (100, 1),
        (4759, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts) == [value]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 10),
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (100, 20)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [
        (1, 2, [0, 1]),
        (1, 7, [0, 0, 0, 0, 0, 0, 1]),
        (3, 10, [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int,
    expected_result: list
) -> None:
    assert split_integer(value, number_of_parts) == expected_result
