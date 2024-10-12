from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goal = split_integer(16, 4)
    assert sum(goal) == 16


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goal = split_integer(6, 2)
    assert goal[0] == goal[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goal = split_integer(8, 1)
    assert goal == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goal = split_integer(1, 5)
    assert goal == [0, 0, 0, 0, 1]
