from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert parts == [4,4,4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 12
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert parts == [12]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert sorted(parts) == parts


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert len(parts) == number_of_parts
    assert parts.count(0) == 2
    assert sum(parts) == value
