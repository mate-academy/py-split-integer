from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert 10 == sum(split_integer(10, 5))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 20
    parts = 4
    result = split_integer(value, parts)
    assert len(result) == parts
    assert all(part == value // parts for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 15
    parts = 1
    result = split_integer(value, parts)
    assert result == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    parts = 8
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
