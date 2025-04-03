from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(5, 2)
    assert sum(result) == 5
    assert max(result) - min(result) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(5, 1)
    assert result == [5]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 3)
    assert result == [0, 1, 1]


def test_should_handle_more_parts_than_value() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]


def test_should_handle_large_values() -> None:
    result = split_integer(1000, 7)
    assert sum(result) == 1000
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
