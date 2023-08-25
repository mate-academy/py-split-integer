import copy

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goals = split_integer(5, 3)
    assert sum(goals) == 5


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goals = split_integer(9, 3)
    assert goals[0] == goals[1] == goals[2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goals = split_integer(4, 1)
    assert goals[0] == 4


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goals = split_integer(32, 6)
    sorted_goals = copy.copy(goals)
    sorted_goals.sort()
    assert goals == sorted_goals


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goals = split_integer(1, 2)
    required_list = [0, 1]
    assert goals == required_list
