from app.split_integer import split_integer
import  pytest

def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(49, 7)) == 49


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(set(split_integer(6, 3))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(7, 1) == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 7) == [0, 0, 1, 1, 1, 1, 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 7) == [0, 0, 1, 1, 1, 1, 1]


def test_should_return_error_when_value_is_None() -> None:
    with pytest.raises(TypeError):
        split_integer(None, 6)

def test_should_return_error_when_number_of_parts_is_None() -> None:
    with pytest.raises(TypeError):
        split_integer(5, None)

