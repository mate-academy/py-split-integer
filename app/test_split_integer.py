import pytest  # noqa: F401
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 0, 1, 2]


def test_expected_examples_directly() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


@pytest.mark.parametrize("value, parts", [
    (3, 5),
    (7, 7),
    (8, 1),
    (100, 9),
])
def test_general_properties(value: int, parts: int) -> None:
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
