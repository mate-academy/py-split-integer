import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, 8),
        (0, 2, 0),
        (17, 4, 17),
        (32, 6, 32)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int, result: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == result


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, 1),
        (0, 0, 0),
        (17, 4, 4),
        (32, 6, 6)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int, result: int
) -> None:
    assert len(split_integer(value, number_of_parts)) == result


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (0, 0, []),
        (17, 1, [17]),
        (32, 1, [32])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, number_of_parts: int, result: int
) -> None:
    assert split_integer(value, number_of_parts) == result


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int, result: int
) -> None:
    assert split_integer(value, number_of_parts) == result


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (0, 3, [0, 0, 0]),
        (17, 4, [4, 4, 4, 5])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, number_of_parts: int, result: int
) -> None:
    assert split_integer(value, number_of_parts) == result
