from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(17, 3)) == 17
    ), "Result not equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(700, 5) == [140, 140, 140, 140, 140]
    ), "Parts of list is not equal to each other"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(1234, 1) == [1234]
    ), "Result not equal to value when it split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Parts must be sorted but they not"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 4) == [0, 0, 0, 1]
    ), "Response list must contain 3 leading zero's"
