from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goal = split_integer(6, 2)
    assert (
        sum(goal) == 6
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goal = split_integer(6, 2)
    assert len(goal) == 2
    assert goal[0] == goal[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goal = split_integer(8, 1)
    assert goal == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goal = split_integer(17, 4)
    assert sorted(goal) == goal


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goal = split_integer(10, 4)
    assert len(goal) == 4
    assert all(element == 0 for element in goal)


def test_could_split_on_different_parts() -> None:
    goal = split_integer(10, 3)
    assert len(set(goal)) != 1
