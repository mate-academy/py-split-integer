from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 20, 5
    result = split_integer(value, parts)
    assert all(x == 4 for x in result)
    assert result == sorted(result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 7, 1
    result = split_integer(value, parts)
    assert result == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)
    assert sum(result) == value
    assert result.count(0) == 2
    assert sorted(result) == result
    assert max(result) - min(result) <= 1
