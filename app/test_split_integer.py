from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    res = split_integer(16, 3)
    assert sum(res) == 16


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    res = split_integer(18, 3)
    assert len(set(res)) == 1


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    res = split_integer(8, 1)
    assert res == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    res = split_integer(64, 12)
    assert res == sorted(res)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    res = split_integer(5, 10)
    assert res == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]