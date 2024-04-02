import pytest

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(100, 3)) == 100


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(100, 4).count(25) == 4


@pytest.mark.parametrize(
    "numbers,expected_result",
    [
        pytest.param(split_integer(10, 1), [10]),
        pytest.param(split_integer(10, 10), [1] * 10)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    numbers: list, expected_result: int
) -> None:
    assert numbers == expected_result


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(100, 3) == [33, 33, 34]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
