from split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value, (f"Sum of parts {sum(parts)} "
                                 f"does not equal original value {value}")
    print("Test passed!")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert all(part == parts[0] for part in parts), \
        f"Parts {parts} are not equal"
    print("Test passed!")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 12
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert len(parts) == 1, f"Expected one part, but got {len(parts)}"
    assert parts[0] == value, (f"Expected part to equal {value}, "
                               f"but got {parts[0]}")
    print("Test passed!")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 11
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts), f"Parts {parts} are not sorted"
    print("Test passed!")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 12
    number_of_parts = 13
    parts = split_integer(value, number_of_parts)
    assert parts[0] == 0, f"Expected part to equal 0, but got {parts[0]}"
    print("Test passed!")
