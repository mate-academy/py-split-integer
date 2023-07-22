from app.split_integer import split_integer


def test_sum_of_the_parts_equal_to_value() -> None:
    assert sum(split_integer(15, 3)) == 15


def test_split_equal_when_value_divisible_by_parts() -> None:
    assert len(split_integer(10, 2)) == 2


def test_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]


def test_parts_sorted_when_they_are_not_equal() -> None:
    assert split_integer(11, 3) == sorted(split_integer(11, 3))


def test_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
