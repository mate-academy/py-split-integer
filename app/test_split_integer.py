from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    part = 4
    assert sum(split_integer(value, part)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    part = 2
    assert split_integer(value, part).count(value // part) == part


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    part = 1
    assert split_integer(value, part) == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    part = 6
    assert sorted(split_integer(value, part)) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    part = 3
    assert split_integer(value, part) == [0, 1, 1]
