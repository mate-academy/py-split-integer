from app.split_integer import split_integer


def test_sum_of_the_parts_are_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_split_into_equal_parts_when_value_is_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_part_equals_to_a_value_when_slitting_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_not_equal_parts_are_sorted() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 7) == [0, 0, 1, 1, 1, 1, 1]
