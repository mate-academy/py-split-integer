from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(9, 2)) == 9


def test_split_into_equal_parts_when_value_is_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_return_part_equals_to_a_value_when_slitting_into_one_part() -> None:
    assert split_integer(9, 1) == [9]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1]
