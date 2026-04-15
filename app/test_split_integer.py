from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(17, 4)
    assert sum(parts) == 17, \
        "Sum of the parts should be equal to 17"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(9, 3)
    assert parts[0] == parts[1] == parts[2], \
        "Method should split number 9 into [3, 3, 3]"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(3, 1) == [3], \
        "Method should return 3 when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], \
        "Parts should be sorted by ascending"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1], \
        "Method should return zero when value is less than number of parts"
