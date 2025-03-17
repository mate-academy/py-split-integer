from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    ls = split_integer(6, 3)
    assert sum(ls) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    ls = split_integer(6, 3)
    assert len(ls) == 3


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    ls = split_integer(6, 1)
    assert len(ls) == 1 and ls[0] == 6


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    ls = split_integer(32, 6)
    assert ls == sorted(ls)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    ls = split_integer(4, 5)
    assert ls == [0, 1, 1, 1, 1]
