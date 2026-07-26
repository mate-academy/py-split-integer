from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, "Sum of parts should equal the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4], f"Expected [4, 4, 4], but got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 12
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [12], f"Expected [12], but got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4, 5], f"Expected [4, 4, 4, 5], but got {result}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 0, 1], f"Expected [0, 0, 0, 1], but got {result}"


def test_should_not_increment_only_last_part_when_remainder_exists() -> None:
    value = 7
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == [2, 2, 3], f"Expected [2, 2, 3], but got {result}"


def test_should_distribute_remainder_evenly_across_parts() -> None:
    value = 9
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [2, 2, 2, 3], f"Expected [2, 2, 2, 3], but got {result}"


def test_parts_should_be_sorted_even_with_remainder() -> None:
    value = 8
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == [2, 3, 3], f"Expected [2, 3, 3], but got {result}"