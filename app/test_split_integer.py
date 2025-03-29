from app.split_integer import split_integer

goal_long = split_integer(32, 6)
goal_short = split_integer(8, 1)


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(goal_long) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for i in range(len(goal_long) - 1):
        assert abs(goal_long[i] - goal_long[i + 1]) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert goal_short == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert goal_long == sorted(goal_long)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 8) == [0, 0, 0, 0, 0, 0, 1, 1]


def test_other_function_cant_be_used_instead_of_original() -> None:
    assert split_integer.__name__ == "split_integer"
