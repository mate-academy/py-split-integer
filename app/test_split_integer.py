from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    assert (sum(split_integer(value, number_of_parts)) == value), \
        (f"sum of {split_integer(value, number_of_parts)} "
            f"should be equal to {value}")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (split_integer(6, 2) == [3, 3]), \
        f"{split_integer(6, 2)} should be equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(8, 1) == [8]), \
        f"length of {split_integer(8, 1)} should 1"


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int, result: list
) -> None:
    func = split_integer(value, number_of_parts)
    expected = sorted(func)
    assert (func == expected), \
        f"{split_integer(value, number_of_parts)} should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]), \
        "'split_integer' should add zeros"
