from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    actual = split_integer(17, 4)
    assert sum(actual) == 17


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    actual = split_integer(16, 4)
    assert actual == [4, 4, 4, 4]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    actual = split_integer(8, 1)
    assert actual == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    actual = split_integer(17, 4)
    assert actual == sorted(actual)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    actual = split_integer(3, 4)
    assert actual == [0, 1, 1, 1]
