from app.split_integer import split_integer


def test_sum_of_parts_equals_original_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(0, 3)) == 0


def test_equal_parts_when_value_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(100, 10) == [10] * 10


def test_single_part_equals_value() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(0, 1) == [0]
    assert split_integer(999, 1) == [999]


def test_parts_are_sorted_and_difference_is_at_most_one() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_zeros_are_added_when_value_is_less_than_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(0, 4) == [0, 0, 0, 0]
    assert split_integer(2, 6) == [0, 0, 0, 0, 1, 1]
