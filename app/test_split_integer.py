from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:

    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goal = split_integer(30, 6)

    assert all(num == 5 for num in goal)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goal = split_integer(32, 1)
    assert goal[0] == 32


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goal = split_integer(32, 6)
    assert goal == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goal = split_integer(2, 3)
    assert goal == [0, 1, 1]
