from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    expected_value = 32
    assert sum(parts) == expected_value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    parts = split_integer(value, number_of_parts)
    expected_value = value // number_of_parts

    assert all(expected_value == item for item in parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    expected = [8]
    assert result == expected


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    expected_value = [4, 4, 4, 5]
    assert result == expected_value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 8)
    expected_value = []
    assert result == expected_value
