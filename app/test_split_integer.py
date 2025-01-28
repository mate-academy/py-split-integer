from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    parts = 2
    result = split_integer(value, parts)
    assert result == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    result = split_integer(value, parts)
    assert result == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    parts = 6
    result = split_integer(value, parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert result == [4, 4, 4, 5]
