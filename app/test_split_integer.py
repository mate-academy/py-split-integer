from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(32, 8) == [4, 4, 4, 4, 4, 4, 4, 4]
    assert split_integer(32, 4) == [8, 8, 8, 8]
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_difference_between_max_and_min_should_be_no_more_than_one() -> None:
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 6) == [0, 0, 0, 1, 1, 1]


def test_should_return_exact_number_of_parts() -> None:
    assert len(split_integer(15, 4)) == 4
