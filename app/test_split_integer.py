from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts_of_number = split_integer(16, 4)
    assert sum(parts_of_number) == 16


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts_of_number = split_integer(8, 2)
    assert parts_of_number == [4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts_of_number = split_integer(10, 1)
    assert parts_of_number == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts_of_number = split_integer(15, 2)
    assert parts_of_number == sorted(parts_of_number)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts_of_number = split_integer(2, 6)
    assert parts_of_number == [0, 0, 0, 0, 1, 1]
