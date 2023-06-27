from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goals = split_integer(8, 1)
    assert sum(goals) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goals = split_integer(6, 2)
    assert goals == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goals = split_integer(6, 2)
    assert goals == [3, 3]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goals = split_integer(17, 4)
    assert goals == sorted(goals)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goals = split_integer(3, 5)
    assert goals == [0, 0, 1, 1, 1]
