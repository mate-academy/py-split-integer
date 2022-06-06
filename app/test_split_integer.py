from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value = 10
    number_of_parts = 2
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value = 10
    number_of_parts = 2
    assert split_integer(value, number_of_parts). \
        count(value / number_of_parts) == \
           number_of_parts


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 10
    number_of_parts = 1
    assert split_integer(value, number_of_parts) == [value]


def test_parts_should_be_sorted_when_they_are_not_equal():
    value = 10
    number_of_parts = 3
    assert split_integer(value, number_of_parts) == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value = 2
    number_of_parts = 10
    assert split_integer(value, number_of_parts) == \
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
