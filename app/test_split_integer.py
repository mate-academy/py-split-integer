from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(777, 30) == [25] * 3 + [26] * 27


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(20, 4) == [5, 5, 5, 5]
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(25, 1) == [25]
    assert split_integer(15, 1) == [15]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(23, 3) == [7, 8, 8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(6, 8) == [0, 0, 1, 1, 1, 1, 1, 1]
