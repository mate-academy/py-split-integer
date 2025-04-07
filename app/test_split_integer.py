from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 1)) == 10
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(2, 7)) == 2
    assert sum(split_integer(0, 2)) == 0


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(4, 4) == [1, 1, 1, 1]
    assert split_integer(7, 1) == [7]
    assert split_integer(0, 2) == [0, 0]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    res = split_integer(17, 4)
    assert res == sorted(res)

    res = split_integer(32, 6)
    assert res == sorted(res)

    res = split_integer(3, 2)
    assert res == sorted(res)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2) == [0, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
    assert split_integer(0, 3) == [0, 0, 0]
