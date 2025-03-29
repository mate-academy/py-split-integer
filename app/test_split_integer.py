from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    actual = split_integer(6, 2)
    assert sum(actual) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 2
    actual = split_integer(value, number_of_parts)
    assert actual == [5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    actual = split_integer(8, 1)
    assert actual[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    actual = split_integer(17, 4)
    assert actual == sorted(actual)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    actual = split_integer(2, 3)
    assert actual == [0, 1, 1]
