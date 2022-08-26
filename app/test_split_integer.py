from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    result = split_integer(8, 1)
    assert sum(result) == 8

    result = split_integer(6, 2)
    assert sum(result) == 6

    result = split_integer(17, 4)
    assert sum(result) == 17

    result = split_integer(32, 6)
    assert sum(result) == 32


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    result = split_integer(6, 2)
    assert len(result) == 2

    result = split_integer(17, 4)
    assert len(result) == 4

    result = split_integer(32, 6)
    assert len(result) == 6


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    result = split_integer(8, 1)
    assert result[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal():
    result = split_integer(17, 4)
    assert result == sorted(result)

    result = split_integer(32, 6)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    result = split_integer(5, 6)
    assert result == [0, 1, 1, 1, 1, 1]

    result = split_integer(0, 3)
    assert 0 in result
