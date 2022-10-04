from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    assert 17 == sum(split_integer(17, 4))


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    result = split_integer(40, 5)
    assert 0 == (result[-1] - result[0])


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert 1 == len(split_integer(25, 1))


def test_parts_should_be_sorted_when_they_are_not_equal():
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    result = split_integer(4, 9)
    assert 5 == result.count(0)
