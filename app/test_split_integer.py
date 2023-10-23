from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 28, 4
    result = split_integer(value, parts)
    assert all([result[i - 1] == result[i] for i in range(1, len(result))])


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 293, 1
    result = split_integer(value, parts)
    assert result == [293]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 32, 6
    result = split_integer(value, parts)
    assert all([result[i - 1] <= result[i] for i in range(1, len(result))])


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)
    assert result == [0, 0, 1, 1, 1]


def test_difference_between_min_and_max_should_be_1() -> None:
    value, parts = 29, 6
    result = split_integer(value, parts)
    assert max(result) - min(result) <= 1
