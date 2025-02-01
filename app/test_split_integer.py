from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 8
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, (
        "The sum of parts is not equal to the original value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    assert result == [3, 3], f"Expected [3, 3], got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [8], f"Expected [8], got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == sorted(result), f"Result list is not sorted: {result}"
    assert max(result) - min(result) <= 1, (
        "Difference between max and min parts is greater than 1"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, (
        "The sum of parts is not equal to the original value"
    )
    assert len(result) == number_of_parts, (
        f"Result list length ({len(result)}) does not match "
        f"the number of parts ({number_of_parts})"
    )
    assert result == sorted(result), f"Result list is not sorted: {result}"
    assert max(result) - min(result) <= 1, (
        "Difference between max and min parts is greater than 1"
    )
    assert result.count(0) == 3, f"Expected 3 zeros, got {result.count(0)}"
