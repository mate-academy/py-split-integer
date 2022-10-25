from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 5)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(18, 3) == [6, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(27, 1) == [27]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(36, 7) == sorted(split_integer(36, 7))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1]
