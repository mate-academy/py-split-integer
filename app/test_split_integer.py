from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value, \
        f"Expected sum of {value}, but got {sum(result)}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 6, 2
    result = split_integer(value, parts)
    assert result == [3, 3], f"Expected [3, 3], got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 4, 1
    result = split_integer(value, parts)
    assert result == [value], f"Expected [{value}], got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 21, 4
    result = split_integer(value, parts)
    assert result == sorted(result), f"Expected sorted result, got {result}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)
    assert result == [0, 0, 1, 1, 1], f"Expected [0, 0, 1, 1, 1], got {result}"
