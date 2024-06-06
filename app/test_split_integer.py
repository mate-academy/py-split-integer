from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 3)) == 8
    assert sum(split_integer(12, 4)) == 12
    assert sum(split_integer(20, 5)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(12, 1) == [12]
    assert split_integer(20, 1) == [20]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(8, 3) == sorted([2, 3, 3])
    assert split_integer(12, 5) == sorted([2, 2, 2, 3, 3])
    assert split_integer(20, 4) == sorted([5, 5, 5, 5])


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(8, 10) == [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    assert (split_integer(12, 15)
            == [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert (split_integer(20, 25)
            == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
