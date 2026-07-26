from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value
    assert len(result) == parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 6, 2
    assert split_integer(value, parts) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 8, 1
    assert split_integer(value, parts) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_example_case_thirty_two_divided_into_six_parts() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
