from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    result = split_integer(10, 2)

    assert sum(result) == 10


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    result = split_integer(10, 2)

    assert result == [5, 5]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    result = split_integer(3, 1)

    assert result == [3]


def test_parts_should_be_sorted_when_they_are_not_equal():
    result = split_integer(10, 3)

    assert result == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    result = split_integer(5, 6)

    assert result == [0, 1, 1, 1, 1, 1]
