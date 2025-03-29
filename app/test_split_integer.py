from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goals = split_integer(8, 1)
    assert goals == [8], f"Expected [8], but got {goals}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    goals = split_integer(6, 2)
    assert goals == [3, 3], f"Expected [3, 3], but got {goals}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goals = split_integer(17, 4)
    assert goals == [4, 4, 4, 5], f"Expected [4, 4, 4, 5], but got {goals}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goals = split_integer(32, 6)
    assert goals == [5, 5, 5, 5, 6, 6], \
        f"Expected [5, 5, 5, 5, 6, 6], but got {goals}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goals = split_integer(1, 2)
    assert goals == [0, 1], f"Expected [0, 1], but got {goals}"
