from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    num_parts = 5
    res = split_integer(value, num_parts)
    assert sum(res) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected = split_integer(10, 5)
    result = [2, 2, 2, 2, 2]
    assert expected == result


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    expected = split_integer(2, 1)
    result = [2]
    assert expected == result


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    expected = split_integer(2, 3)
    result = sorted(expected)
    assert result == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    expected = split_integer(2, 3)
    result = [0, 1, 1]
    assert expected == result
