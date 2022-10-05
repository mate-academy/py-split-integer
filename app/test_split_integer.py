from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    assert 17 == sum(split_integer(17, 4))


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert [8, 8, 8, 8, 8] == split_integer(40, 5)


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert 1 == len(split_integer(25, 1))


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert [5, 5, 5, 5, 6, 6] == sorted(split_integer(32, 6))


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert 5 == split_integer(4, 9).count(0)
