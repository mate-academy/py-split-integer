from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    parts = split_integer(10, 3)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    expected = [3, 3, 3, 3]
    assert result == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(10, 3)
    assert parts == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(2, 4)
    assert parts == [0, 0, 1, 1]
