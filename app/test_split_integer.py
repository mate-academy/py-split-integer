# from app.split_integer import split_integer
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, (
        "Sum of the function result with value {17} "
        "and number {6} should be equal to {17}"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(49, 7) == [7, 7, 7, 7, 7, 7, 7], (
        "Value should split into equal parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "Result should be equal to value when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "Result list should be sorted"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1], (
        "Result should contain zeros when value is less than number of parts"
    )
