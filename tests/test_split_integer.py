from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    result = split_integer(15, 3)
    assert sum(result) == 15


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    result = split_integer(20, 4)
    assert result == [5, 5, 5, 5]


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    result = split_integer(13, 1)
    assert result == [13]


def test_parts_should_be_sorted_when_they_are_not_equal():
    result = split_integer(21, 4)
    assert result == [5, 5, 5, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    result = split_integer(2, 3)
    assert result == [0, 1, 1]
