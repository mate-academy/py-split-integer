from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(100, 7)) == 100
    assert sum(split_integer(1, 5)) == 1
    assert sum(split_integer(2, 5)) == 2


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> (
    None
):
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(8, 2) == [4, 4]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 4) == [5, 5, 5, 5]
    assert split_integer(100, 5) == [20, 20, 20, 20, 20]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> (
    None
):
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]
    assert split_integer(1, 1) == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1
    assert split_integer(32, 6) == sorted(split_integer(32, 6))
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1
    assert split_integer(10, 3) == sorted(split_integer(10, 3))
    assert max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1
    assert split_integer(7, 3) == sorted(split_integer(7, 3))
    assert max(split_integer(7, 3)) - min(split_integer(7, 3)) <= 1
    assert split_integer(15, 4) == sorted(split_integer(15, 4))
    assert max(split_integer(15, 4)) - min(split_integer(15, 4)) <= 1
    assert split_integer(25, 5) == sorted(split_integer(25, 5))
    assert max(split_integer(25, 5)) - min(split_integer(25, 5)) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 5) == sorted(split_integer(1, 5))
    assert max(split_integer(1, 5)) - min(split_integer(1, 5)) <= 1
    assert sum(split_integer(1, 5)) == 1
    assert split_integer(2, 5) == sorted(split_integer(2, 5))
    assert max(split_integer(2, 5)) - min(split_integer(2, 5)) <= 1
    assert sum(split_integer(2, 5)) == 2
    assert split_integer(3, 5) == sorted(split_integer(3, 5))
    assert max(split_integer(3, 5)) - min(split_integer(3, 5)) <= 1
    assert sum(split_integer(3, 5)) == 3
    assert split_integer(4, 5) == sorted(split_integer(4, 5))
    assert max(split_integer(4, 5)) - min(split_integer(4, 5)) <= 1
    assert sum(split_integer(4, 5)) == 4
    assert split_integer(1, 10) == sorted(split_integer(1, 10))
    assert max(split_integer(1, 10)) - min(split_integer(1, 10)) <= 1
    assert sum(split_integer(1, 10)) == 1
