from app.split_integer import split_integer


def test_difference_between_max_and_min_should_not_exceed_one() -> None:
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1
    assert max(split_integer(5, 2)) - min(split_integer(5, 2)) <= 1


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(5, 10)) == 5


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(15, 1) == [15]
    assert split_integer(1, 1) == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(5, 2) == [2, 3]
