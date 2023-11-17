from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(32, 6)
    assert sum(parts) == 32, "Sum of parts should equal the value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = sorted(split_integer(32, 8))
    assert parts[0] == parts[-1], \
        "All parts should be equal if value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1)
    assert parts[0] == 8, "Part should equal value when split into 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4)
    assert parts == sorted(parts), "Parts list should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(1, 3)
    assert parts == [0, 0, 1], \
        "List should have zeros if value is smaller than number of parts"
