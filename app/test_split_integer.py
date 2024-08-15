from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 20
    assert sum(split_integer(value, 5)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goal = split_integer(15, 3)
    assert goal == [5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goal = split_integer(17, 4)
    assert goal == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goal = split_integer(3, 7)
    assert goal == [0, 0, 0, 0, 1, 1, 1]
