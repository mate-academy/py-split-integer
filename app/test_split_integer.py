from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(10, 3)
    assert sum(parts) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    actual_parts = split_integer(15, 3)
    assert actual_parts == [5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(15, 1)
    assert parts[0] == 15


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(15, 4)
    assert parts == [3, 4, 4, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(2, 4)
    assert parts == [0, 0, 1, 1]
