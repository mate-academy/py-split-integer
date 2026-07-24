import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 1),
        (100, 19),
        (12, 11)

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
        (20, 10),
        (60, 15),
        (1000, 50)

    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(
        value,
        number_of_parts
    )[0] == split_integer(
        value,
        number_of_parts
    )[-1]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 1),
        (9, 1),
        (1000, 1)

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
        (20, 9),
        (4, 3),
        (1000, 54)

    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(
        value,
        number_of_parts
    ) == sorted(split_integer(
        value,
        number_of_parts
    ))


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (20, 21),
        (0, 10),
        (10, 19)

    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert 0 in split_integer(value, number_of_parts)
