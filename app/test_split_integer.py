from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value, (
        "The sum of the parts should equal the original value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert all(part == 4 for part in parts), (
        "All parts should be equal when the value is divisible by the parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert parts == [8], "If one part, the result should be the original value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts), (
        "The parts should be sorted in ascending order"
    )


def test_difference_between_min_and_max_should_be_no_more_than_one() -> None:
    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert max(parts) - min(parts) <= 1, (
        "The difference between the max and min part should be <= 1"
    )
