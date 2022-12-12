from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goals = split_integer(6, 2)

    assert sum(goals) == 6, "Sum of array should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goals = split_integer(6, 2)

    assert all(part == goals[0] for part in goals), \
        "All elements of array should be equal"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goals = split_integer(8, 1)

    assert len(goals) == 1, "Array should have only 1 element"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goals = split_integer(17, 4)

    assert sorted(goals) == goals, "Array should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goals = split_integer(3, 4)

    assert goals.count(0) == 1, "Array should add correct number of zeros"
