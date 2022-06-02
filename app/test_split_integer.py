from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    goal = split_integer(32, 6)
    assert sum(goal) == 32


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    goal = split_integer(9, 3)
    assert len(set(goal)) == 1


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    goal = split_integer(8, 1)
    assert goal == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    goal = split_integer(32, 6)
    assert goal == sorted(goal)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    goal = split_integer(3, 9)
    assert goal == [0, 0, 0, 0, 0, 0, 1, 1, 1]
