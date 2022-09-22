from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(6, 2)) == 6


def test_should_split_a_number_into_equal_parts():
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_value_when_slitting_into_one_part():
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(32, 6) == sorted(split_integer(32, 6))


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(2, 4) == [0, 0, 1, 1]
