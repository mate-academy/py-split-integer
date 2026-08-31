from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 4)) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(8, 4) == [2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(9, 4) == [2, 2, 2, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2) == [0, 1]


def test_should_check_difference_between_max_and_min_values_of_parts() -> None:
    assert max(split_integer(9, 4)) - min(split_integer(9, 4)) <= 1


def test_should_compare_len_of_parts_and_number_of_parts() -> None:
    assert len(split_integer(21, 3)) == 3


def test_only_last_number_is_incremented() -> None:
    assert split_integer(8, 3) == [2, 3, 3]
