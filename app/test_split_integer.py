import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(6, 0, 0, id="0 part"),
        pytest.param(0, 4, 0, id="value = 0"),
        pytest.param(6, 2, 6, id="2 part")
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == result


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 2)[0] == split_integer(10, 2)[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 6) == [0, 0, 0, 1, 1, 1]
