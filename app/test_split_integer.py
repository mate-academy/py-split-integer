from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert split_integer(100, 2) == [50, 50]


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert split_integer(80, 4) == [20, 20, 20, 20]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(50, 1) == [50]


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(20, 3) == [6, 7, 7]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
