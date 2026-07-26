from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 11
    number_of_parts = 3
    goals = split_integer(value, number_of_parts)
    assert value == sum(goals)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goals = split_integer(7, 14)
    assert goals == sorted(goals)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5
    goals = split_integer(value, number_of_parts)
    assert goals == [0, 0, 0, 1, 1]
    assert number_of_parts == len(goals)


def test_max_min_1() -> None:
    value = 32
    number_of_parts = 6
    goals = split_integer(value, number_of_parts)
    assert max(goals) - min(goals) <= 1
