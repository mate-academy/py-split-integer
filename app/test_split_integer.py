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
def test_sum_of_the_parts_should_be_equal_to_value(value, number_of_parts) -> None: # noqa
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (6, 2),
        (10, 2),
        (50, 2)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(value, number_of_parts) -> None: # noqa
    result = split_integer(value, number_of_parts)
    assert len(result) == 2 and result[0] == result[1]


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (5, 1),
        (7, 1),
        (10, 1),
        (20, 1),
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(value, number_of_parts) -> None: # noqa
    result = split_integer(value, number_of_parts)
    assert len(result) == 1 and result[0] == value


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (32, 6),
        (52, 8)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(value, number_of_parts) -> None: # noqa
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 2),
        (50, 100),
        (6, 29)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(value, number_of_parts) -> None: # noqa
    result = split_integer(value, number_of_parts)
    assert set(result) == {0, 1}
