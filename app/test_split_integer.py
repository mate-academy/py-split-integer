from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 8
    parts = 1
    actual = sum(split_integer(value, parts))
    expected = 8
    assert (actual == expected)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    parts = 2
    actual = len(set(split_integer(value, parts)))
    expected = 1
    assert (actual == expected)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    actual = split_integer(value, parts)[0]
    expected = 8
    assert (actual == expected)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    parts = 4
    actual = split_integer(value, parts)
    expected = [4, 4, 4, 5]
    assert (actual == expected)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    parts = 4
    actual = split_integer(value, parts)
    expected = [0, 0, 1, 1]
    assert (actual == expected)
