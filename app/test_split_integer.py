from app import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer.split_integer(8, number_of_parts=2)) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(8, number_of_parts=2) == [4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, number_of_parts=1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer.split_integer(17, number_of_parts=4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(2, number_of_parts=5) == [0, 0, 0, 1, 1]


def test_should_distribute_remainder_between_last_parts() -> None:
    assert split_integer.split_integer(
        32, number_of_parts=6
    ) == [5, 5, 5, 5, 6, 6]


def test_should_split_into_three_parts() -> None:
    assert split_integer.split_integer(10, number_of_parts=3) == [3, 3, 4]


def test_should_split_into_two_unequal_parts() -> None:
    assert split_integer.split_integer(5, number_of_parts=2) == [2, 3]


def test_should_add_zeros_for_one_value_and_three_parts() -> None:
    assert split_integer.split_integer(1, number_of_parts=3) == [0, 0, 1]
