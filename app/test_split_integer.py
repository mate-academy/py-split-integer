from app.split_integer import split_integer


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_length_should_be_equal_to_number_of_parts() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]


def test_difference_between_min_and_max_should_be_no_more_than_one() -> None:
    assert split_integer(23, 5) == [4, 4, 5, 5, 5]
    assert split_integer(100, 9) == [11, 11, 11, 11, 11, 11, 11, 11, 12]
    assert split_integer(7, 3) == [2, 2, 3]


def test_should_distribute_remainder_correctly() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(10, 4) == [2, 2, 3, 3]


def test_should_handle_multiple_cases_precisely() -> None:
    assert split_integer(7, 3) == [2, 2, 3]
    assert split_integer(14, 4) == [3, 3, 4, 4]
    assert split_integer(9, 5) == [1, 2, 2, 2, 2]


def test_small_edge_cases() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(2, 3) == [0, 1, 1]


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(20, 4) == [5, 5, 5, 5]
    assert split_integer(7, 3) == [2, 2, 3]
    assert split_integer(100, 9) == [11, 11, 11, 11, 11, 11, 11, 11, 12]
