from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value = 32
    number_of_parts = 6
    res = split_integer(value, number_of_parts)
    assert sum(res) == value


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value = 6
    number_of_parts = 2
    res = split_integer(value, number_of_parts)
    assert res == [3, 3]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 8
    number_of_parts = 1
    res = split_integer(value, number_of_parts)
    assert res == [value]


def test_parts_should_be_sorted_when_they_are_not_equal():
    value = 17
    number_of_parts = 4
    res = split_integer(value, number_of_parts)
    assert res == sorted(res)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value = 2
    number_of_parts = 5
    res = split_integer(value, number_of_parts)
    assert res == [0, 0, 0, 1, 1]
