from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value = 32
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value = 8
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    assert result[0] % result[1] == 0


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [value]


def test_parts_should_be_sorted_when_they_are_not_equal():
    value = 32
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert result == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value = 4
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 1, 1, 1, 1]
