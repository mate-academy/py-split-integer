from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 20
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    expected_part_value = value // number_of_parts
    assert all(part == expected_part_value for part in parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 5
    number_of_parts = 1
    assert len(split_integer(value, number_of_parts)) == number_of_parts


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 20
    number_of_parts = 6
    assert split_integer(value, number_of_parts) == \
           sorted(split_integer(value, number_of_parts))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5
    assert split_integer(value, number_of_parts) == [0, 0, 0, 1, 1]
