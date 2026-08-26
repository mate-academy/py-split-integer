from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goal = split_integer(11, 3)
    assert sum(goal) == 11


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goal = split_integer(6, 2)
    assert goal == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goal = split_integer(4, 1)
    assert goal == [4]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goal = split_integer(17, 4)
    assert goal == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goal = split_integer(2, 6)
    assert goal == [0, 0, 0, 0, 1, 1]
