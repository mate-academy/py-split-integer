from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value = 17
    number_of_parts = 4

    goal = split_integer(value, number_of_parts)

    assert sum(goal) == value


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value = 16
    number_of_parts = 4

    goal = split_integer(value, number_of_parts)

    assert len(set(goal)) == 1


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 5
    number_of_parts = 1

    goal = split_integer(value, number_of_parts)

    assert goal == sorted(goal)


def test_parts_should_be_sorted_when_they_are_not_equal():
    value = 17
    number_of_parts = 4

    goal = split_integer(value, number_of_parts)

    assert goal == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value = 2
    number_of_parts = 3

    goal = split_integer(value, number_of_parts)

    assert goal == [0, 1, 1]
