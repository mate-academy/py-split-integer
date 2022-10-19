from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    result = split_integer(value, 4)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 21
    result = split_integer(value, 3)
    assert (result[0] * len(result)) == value


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 4
    result = split_integer(value, 1)
    assert result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    expected = sorted(result)
    assert result == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 3)
    expected = [0, 1, 1]
    assert result == expected
