from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(5, 5)) == 5
    ), "Sum of return values must be equal to 5"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(5, 5) == [1, 1, 1, 1, 1]
    ), "Value should be split to equal parts: 5 / 5 = 1, 1, 1, 1, 1"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(5, 1) == [5]
    ), "Value should return the same value if splitting by 1: 5 / 1 = 5"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(5, 3) == [1, 2, 2]
    ), "Value should be sorted if they are not equal: 5 / 3 = 1, 2, 2"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 3) == [0, 0, 1]
    ), "You must add zeros, when you don't have any integers: 1 / 3 = 0, 0, 1"
