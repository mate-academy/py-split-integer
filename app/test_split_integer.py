import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(8, 1, 8),
        pytest.param(17, 4, 17)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int ,
        number_of_parts: int,
        expected: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(6, 2, [3, 3]),
        pytest.param(32, 4, [8, 8, 8, 8])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(8, 1, [8]),
        pytest.param(17, 1, [17])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int ,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(17, 4, [4, 4, 4, 5]),
        pytest.param(32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(5, 6, [0, 1, 1, 1, 1, 1]),
        pytest.param(3, 5, [0, 0, 1, 1, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected
