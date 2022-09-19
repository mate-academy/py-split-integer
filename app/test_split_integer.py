from app.split_integer import split_integer


def test_sum_should_be_equal_to_value():
    assert sum(split_integer(8, 1)) == 8


def test_split_into_equal_parts_when_value_is_divisible():
    assert split_integer(6, 2) == [3, 3]


def test_part_equals_to_a_value_when_slitting():
    assert split_integer(17, 1) == [17]


def test_sorted_parts_when_not_equal():
    assert split_integer(3, 1) == [3]


def test_should_add_0_when_value_less_than_parts_num():
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
