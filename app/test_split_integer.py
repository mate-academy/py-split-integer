from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value = 17
    number_of_parts = 8

    parts = split_integer(value, number_of_parts)

    assert sum(parts) == 17


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value = 24
    number_of_parts = 8

    parts = split_integer(value, number_of_parts)

    assert parts == [3, 3, 3, 3, 3, 3, 3, 3]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 10
    number_of_parts = 1

    parts = split_integer(value, number_of_parts)

    assert parts[0] == 10


def test_parts_should_be_sorted_when_they_are_not_equal():
    value = 11
    number_of_parts = 3

    parts = split_integer(value, number_of_parts)

    assert parts == [3, 4, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value = 8
    number_of_parts = 10

    parts = split_integer(value, number_of_parts)

    assert parts[:number_of_parts - value] == [0, 0]
