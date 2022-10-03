from app.split_integer import split_integer


def test_should_sum_the_parts():
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts():
    assert split_integer(16, 4) == [4, 4, 4, 4]


def test_return_part_equals_to_a_value():
    assert split_integer(173, 1) == [173]


def test_parts_should_be_sorted():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros():
    assert split_integer(10, 11) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
