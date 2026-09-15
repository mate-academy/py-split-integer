from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    assert sum(split_integer(value, 2)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    number_of_parts = 2
    assert sum(split_integer(6, number_of_parts)) % number_of_parts == 0
    assert sum(split_integer(7, number_of_parts)) % number_of_parts != 0


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 6, 1
    result = split_integer(value, number_of_parts)
    assert result[0] == value
    assert len(result) == number_of_parts


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 6, 7
    result = split_integer(value, number_of_parts)
    assert result[0] == 0
    assert len(result) == number_of_parts


def test_should_return_zeros_when_value_is_zero() -> None:
    assert split_integer(0, 3) == [0, 0, 0]


def test_should_split_into_equal_parts_when_value_equals_to_parts() -> None:
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]
