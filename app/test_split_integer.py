from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 20
    parts = 5
    assert value == sum(split_integer(value, parts))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 20
    parts = 5
    assert [value / parts for _ in range(parts)] == split_integer(value, parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    assert [value] == split_integer(value, parts)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    parts = 6
    assert sorted(split_integer(value, parts)) == split_integer(value, parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 6
    parts = 8
    assert [0] * 2 + [1] * 6 == split_integer(value, parts)
