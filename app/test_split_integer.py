from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    test_list = split_integer(32, 6)
    assert sum(test_list) == 32


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    test_list = split_integer(81, 9)
    assert test_list[::-1] == test_list


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    test_list = split_integer(8, 1)
    assert test_list == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    test_list = split_integer(32, 6)
    assert test_list == sorted(test_list)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    test_list = split_integer(2, 3)
    assert test_list == [0, 1, 1]
