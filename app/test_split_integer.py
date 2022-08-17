from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(36, 6)) == 36 and \
           sum([el for el in split_integer(36, 6) if el == 6]) == 36


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert len(split_integer(36, 6)) == 6


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(6, 1)[0] == 6


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert sorted(split_integer(14, 4), reverse=True) == [4, 4, 3, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(1, 2) == [0, 1]
