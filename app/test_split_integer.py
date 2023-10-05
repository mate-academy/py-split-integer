from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:

    number_of_parts = 5
    value = 30
    assert sum(split_integer(value, number_of_parts)) == 30


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:

    value = 15
    number_of_parts = 3
    assert split_integer(value, number_of_parts) == [5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 15
    number_of_parts = 1
    assert split_integer(value, number_of_parts) == [15]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 29
    number_of_parts = 4
    assert split_integer(value, number_of_parts) == [7, 7, 7, 8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5
    assert split_integer(value, number_of_parts) == [0, 0, 0, 1, 1]
