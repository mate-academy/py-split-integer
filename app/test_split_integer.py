from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    array_of_parts = split_integer(value, 4)
    assert sum(array_of_parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    array_of_parts = split_integer(6, 2)
    assert array_of_parts[0] == array_of_parts[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 8, 1
    array_of_parts = split_integer(value, number_of_parts)
    assert array_of_parts[0] == value and len(array_of_parts) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    array_of_parts = split_integer(17, 4)
    assert array_of_parts == sorted(array_of_parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, numbers_of_parts = 2, 5
    array_of_parts = split_integer(value, numbers_of_parts)
    assert array_of_parts.count(0) == numbers_of_parts - value
