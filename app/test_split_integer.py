from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    func = split_integer(15, 3)
    func2 = split_integer(17, 2)
    assert sum(func) == 15
    assert sum(func2) == 17


def test_should_split_a_number_into_equal_parts():
    assert split_integer(15, 3) == [5, 5, 5]


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(15, 1) == [15]


def test_parts_should_be_sorted_when_they_are_not_equal():
    func = split_integer(17, 3)
    sorted_func = sorted(func)
    assert func == sorted_func


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(7, 8) == [0, 1, 1, 1, 1, 1, 1, 1]
