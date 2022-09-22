from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert 30 == sum(split_integer(30, 4))


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert split_integer(30, 5) == [6, 6, 6, 6, 6]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert [30] == split_integer(30, 1)


def test_parts_should_be_sorted_when_they_are_not_equal():
    pass


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    pass
