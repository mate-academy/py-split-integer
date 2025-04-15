from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert all(part == value // number_of_parts for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 42
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 10
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert result.count(0) == number_of_parts - value
    assert all(part >= 0 for part in result)


def test_uneven_division_with_remainder() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4, 5]


def test_large_value_small_parts() -> None:
    value = 100
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == [33, 33, 34]


def test_small_value_large_parts() -> None:
    value = 5
    number_of_parts = 7
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 1, 1, 1, 1, 1]


def test_equal_value_and_parts() -> None:
    value = 7
    number_of_parts = 7
    result = split_integer(value, number_of_parts)
    assert result == [1, 1, 1, 1, 1, 1, 1]


def test_large_number_of_parts() -> None:
    value = 10
    number_of_parts = 10
    result = split_integer(value, number_of_parts)
    assert result == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_zero_value_multiple_parts() -> None:
    value = 0
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 0, 0, 0]


def test_value_one_multiple_parts() -> None:
    value = 1
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 1]


def test_another_uneven_division() -> None:
    value = 32
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert result == [5, 5, 5, 5, 6, 6]
