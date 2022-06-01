from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value = 32
    goals = split_integer(32, 6)
    assert sum(goals) == value


def test_should_split_a_number_into_equal_parts_when_value_is_divisible():
    goals = split_integer(18, 3)
    assert len(set(goals)) == 1


def test_should_return_a_part_equals_to_a_value_when_one_slitting():
    goals = split_integer(8, 1)
    assert goals == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    goals = split_integer(32, 6)
    assert goals == sorted(goals)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    goals = split_integer(5, 10)
    assert goals == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
