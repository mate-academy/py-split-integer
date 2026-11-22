from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = split_integer(value, 4)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(8, 2)
    assert min(parts) == max(parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1)
    assert parts == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(32, 6)
    assert parts == sorted(parts)
    assert parts == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(1, 5)
    assert parts == [0, 0, 0, 0, 1]
