import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:

    goals = split_integer(value, number_of_parts)

    assert sum(goals) == value


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:

    goals = split_integer(value, number_of_parts)

    assert len(goals) == number_of_parts


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:

    goals = split_integer(value, number_of_parts)

    assert goals == sorted(goals)


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
    ]
)
def test_max_min_difference_should_not_exceed_one(
        value: int,
        number_of_parts: int
) -> None:

    goals = split_integer(value, number_of_parts)

    assert max(goals) - min(goals) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goals = split_integer(8, 1)

    assert goals == [8]
