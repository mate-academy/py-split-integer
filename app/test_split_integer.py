from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(32, 6)) == 32
    ), "Sum of the parts is not equal to the value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(6, 2) == [3, 3]
    ), "The parts should be equal when the value is divisible by them"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), "Returned part should be equals to the value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(22, 4) == [5, 5, 6, 6]
    ), "The parts should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 4) == [0, 1, 1, 1]
    ), "The parts should contain 0 if the value is less than number_of_parts"
