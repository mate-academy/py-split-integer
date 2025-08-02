from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    actual = split_integer(10, 5)

    assert sum(actual) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    actual = split_integer(6, 3)

    assert actual == [2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    actual = split_integer(4, 1)

    assert actual == [4]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    actual = split_integer(5, 3)

    assert actual == [1, 2, 2]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    actual = split_integer(2, 3)

    assert actual == [0, 1, 1]
