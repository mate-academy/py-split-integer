from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(5, 2)) == 5
    assert sum(split_integer(10, 2)) == 10
    assert sum(split_integer(15, 2)) == 15


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(16, 1) == [16]
    assert split_integer(32, 1) == [32]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(7, 3) == [2, 2, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
    assert split_integer(4, 5) == [0, 1, 1, 1, 1]
    assert split_integer(1, 3) == [0, 0, 1]


def test_max_difference_between_parts_is_one() -> None:
    assert max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1
    assert max(split_integer(5, 3)) - min(split_integer(5, 3)) <= 1


def test_returns_correct_number_of_parts() -> None:
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(32, 6)) == 6
    assert len(split_integer(3, 7)) == 7
    assert len(split_integer(1, 5)) == 5


def test_distribution_of_remainder() -> None:
    assert split_integer(11, 4) == [2, 3, 3, 3]
    assert split_integer(13, 5) == [2, 2, 3, 3, 3]
    assert split_integer(10, 4) == [2, 2, 3, 3]
