from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    integers = split_integer(32, 6)
    assert (sum(integers) == 32)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(6, 2)
    assert parts[0] == parts[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1)
    assert parts[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(32, 6)
    assert parts == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(2, 3)
    assert parts == [0]
