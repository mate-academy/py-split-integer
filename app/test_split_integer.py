from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(15, 4)) == 15
    assert sum(split_integer(20, 4)) == 20
    assert sum(split_integer(25, 5)) == 25


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 4) == [5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(15, 1) == [15]
    assert split_integer(20, 1) == [20]
    assert split_integer(25, 1) == [25]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    total = split_integer(15, 4)
    assert total == sorted(total)
    assert max(total) - min(total) <= 1



def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]
    assert split_integer(1, 2) == [0, 1]
    assert split_integer(5, 6) == [0, 1, 1, 1, 1, 1]
