from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert len(split_integer(17, 4)) == 4

    assert sum(split_integer(32, 6)) == 32
    assert len(split_integer(32, 6)) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert sum(split_integer(6, 2)) == 6
    assert len(split_integer(6, 2)) == 2
    assert all(isinstance(x, int) for x in split_integer(6, 2))
    assert split_integer(6, 2) == sorted(split_integer(6, 2))
    assert max(split_integer(6, 2)) - min(split_integer(6, 2)) <= 1

    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert sum(split_integer(8, 4)) == 8
    assert len(split_integer(8, 4)) == 4
    assert all(isinstance(x, int) for x in split_integer(8, 4))
    assert split_integer(8, 4) == sorted(split_integer(8, 4))
    assert max(split_integer(8, 4)) - min(split_integer(8, 4)) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert sum(split_integer(8, 1)) == 8
    assert len(split_integer(8, 1)) == 1
    assert all(isinstance(x, int) for x in split_integer(8, 1))
    assert split_integer(8, 1) == sorted(split_integer(8, 1))

    assert split_integer(1, 1) == [1]
    assert sum(split_integer(1, 1)) == 1
    assert len(split_integer(1, 1)) == 1
    assert all(isinstance(x, int) for x in split_integer(1, 1))
    assert split_integer(1, 1) == sorted(split_integer(1, 1))


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert sum(split_integer(17, 4)) == 17
    assert len(split_integer(17, 4)) == 4
    assert all(isinstance(x, int) for x in split_integer(17, 4))
    assert split_integer(17, 4) == sorted(split_integer(17, 4))
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1

    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert sum(split_integer(32, 6)) == 32
    assert len(split_integer(32, 6)) == 6
    assert all(isinstance(x, int) for x in split_integer(32, 6))
    assert split_integer(32, 6) == sorted(split_integer(32, 6))
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1

    assert sum(split_integer(10, 3)) == 10
    assert len(split_integer(10, 3)) == 3
    assert all(isinstance(x, int) for x in split_integer(10, 3))
    assert split_integer(10, 3) == sorted(split_integer(10, 3))
    assert max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1

    assert sum(split_integer(11, 4)) == 11
    assert len(split_integer(11, 4)) == 4
    assert all(isinstance(x, int) for x in split_integer(11, 4))
    assert split_integer(11, 4) == sorted(split_integer(11, 4))
    assert max(split_integer(11, 4)) - min(split_integer(11, 4)) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert sum(split_integer(1, 2)) == 1
    assert len(split_integer(1, 2)) == 2
    assert all(isinstance(x, int) for x in split_integer(1, 2))
    assert split_integer(1, 2) == sorted(split_integer(1, 2))
    assert max(split_integer(1, 2)) - min(split_integer(1, 2)) <= 1

    assert sum(split_integer(1, 3)) == 1
    assert len(split_integer(1, 3)) == 3
    assert all(isinstance(x, int) for x in split_integer(1, 3))
    assert split_integer(1, 3) == sorted(split_integer(1, 3))
    assert max(split_integer(1, 3)) - min(split_integer(1, 3)) <= 1

    assert split_integer(5, 5) == [1, 1, 1, 1, 1]
    assert sum(split_integer(5, 5)) == 5
    assert len(split_integer(5, 5)) == 5
    assert all(isinstance(x, int) for x in split_integer(5, 5))
    assert split_integer(5, 5) == sorted(split_integer(5, 5))
    assert max(split_integer(5, 5)) - min(split_integer(5, 5)) <= 1

    assert sum(split_integer(3, 5)) == 3
    assert len(split_integer(3, 5)) == 5
    assert all(isinstance(x, int) for x in split_integer(3, 5))
    assert split_integer(3, 5) == sorted(split_integer(3, 5))
    assert max(split_integer(3, 5)) - min(split_integer(3, 5)) <= 1

    assert sum(split_integer(2, 7)) == 2
    assert len(split_integer(2, 7)) == 7
    assert all(isinstance(x, int) for x in split_integer(2, 7))
    assert split_integer(2, 7) == sorted(split_integer(2, 7))
    assert max(split_integer(2, 7)) - min(split_integer(2, 7)) <= 1
