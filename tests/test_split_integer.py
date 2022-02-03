from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(6, 2)) == 6


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    goals = split_integer(20, 4)

    for item in goals[:-1]:
        assert item == 20 / 4


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    goals = split_integer(18, 4)

    assert goals[0] == 4


def test_parts_should_be_sorted_when_they_are_not_equal():
    goals = split_integer(37, 9)
    goals_to_compare = goals[:]

    assert goals_to_compare == sorted(goals)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    goals = split_integer(5, 7)

    for num in range(7 - 5):
        assert goals[num] == 0
