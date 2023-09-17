from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(value=10, number_of_parts=2)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    index_of_parts = split_integer(value=10, number_of_parts=2)
    assert index_of_parts[0] == index_of_parts[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert sum(split_integer(value=10, number_of_parts=1)) == 10


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(value=10, number_of_parts=3) == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    zero_part = split_integer(value=4, number_of_parts=5)
    assert zero_part[0] == 0
