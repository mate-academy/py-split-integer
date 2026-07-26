from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(202, 5)) == 202


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(80, 5) == [16, 16, 16, 16, 16]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(40, 1) == [40]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(77, 3) == [25, 26, 26]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(10, 11) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
