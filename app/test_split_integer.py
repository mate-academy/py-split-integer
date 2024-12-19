from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(20, 5)) == 20

def test_should_split_into_equal_parts_when_value_divisible_by_parts():
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 4) == [5, 5, 5, 5]

def test_should_return_part_equals_to_value_when_split_into_one_part():
    assert split_integer(10, 1) == [10]
    assert split_integer(5, 1) == [5]

def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(13, 4) == [3, 3, 3, 4]
    assert split_integer(23, 6) == [3, 3, 4, 4, 4, 4]

def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(2, 5) == [0, 0, 0, 0, 2]
    assert split_integer(3, 7) == [0, 0, 0, 0, 0, 0, 3]
