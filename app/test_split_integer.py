from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    assert result == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [8]


def test_parts_should_be_sorted_and_evenly() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4, 5]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less() -> None:
    value = 2
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 0, 1, 1]
    assert len(result) == number_of_parts
