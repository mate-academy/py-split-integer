from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    goals = split_integer(3, 3)
    assert goals == [1, 1, 1]


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    goals = split_integer(6, 2)
    assert goals == [3, 3]


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    goals = split_integer(8, 1)
    assert goals == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    goals = split_integer(17, 4)
    assert goals == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    goals = split_integer(2, 3)
    assert goals == [0, 1, 1]
