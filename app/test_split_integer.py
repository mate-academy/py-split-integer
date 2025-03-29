from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(9, 5)) == 9, "parts sum should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(9, 3) == [3, 3, 3], "equal parts expected if possible"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(5, 1) == [5], "same value expected when part = 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(11, 3) == [3, 4, 4], "sorted list expected"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1], "must add zeros if parts > value"
