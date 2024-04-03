from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(32, 6)
    assert sum(parts) == 32, f"The sum of parts {parts} does not equal 32."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], "The value was not split into equal parts when divisible."


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], "The value was not returned as a single part when split into one part."


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], "The parts are not sorted properly when they are not equal."


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1], "Zeros were not properly added when the value is less than the number of parts."
