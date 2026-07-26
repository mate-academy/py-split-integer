from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert len(split_integer(8, 1)) == 1

    assert sum(split_integer(6, 2)) == 6
    assert len(split_integer(6, 2)) == 2

    assert sum(split_integer(17, 4)) == 17
    assert len(split_integer(17, 4)) == 4

    assert sum(split_integer(32, 6)) == 32
    assert len(split_integer(32, 6)) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(15, 3) == [5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(42, 1) == [42]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1

    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1

    assert split_integer(10, 3) == [3, 3, 4]
    assert max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert all(isinstance(x, int) for x in split_integer(2, 5))

    assert split_integer(1, 3) == [0, 0, 1]
    assert all(isinstance(x, int) for x in split_integer(1, 3))

    assert split_integer(0, 4) == [0, 0, 0, 0]
    assert all(isinstance(x, int) for x in split_integer(0, 4))
