from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    actual = sum(split_integer(8, 3))
    expected = 8
    assert actual == expected


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    actual = split_integer(8, 2)
    expected = [4, 4]
    assert actual == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    actual = split_integer(6, 1)
    expected = [6]
    assert actual == expected


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    actual = split_integer(5, 3)
    expected = [1, 2, 2]
    assert actual == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    actual = split_integer(5, 6)
    expected = [0, 1, 1, 1, 1, 1]
    assert actual == expected
