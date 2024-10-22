from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)

    assert sum(parts) == value, "Sum of parts is not equal to the value!"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 15
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)

    assert parts.count(parts[0]) == number_of_parts, "Not all parts are equal!"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)

    assert sum(parts) == value, (
        "Part is not equal to the value if number of parts == 1!"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert parts == [4, 4, 4, 5], (
        "Part is not sorted!"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 6

    assert split_integer(value, number_of_parts) == [0, 0, 0, 1, 1, 1], (
        "Zero is not added!"
    )
