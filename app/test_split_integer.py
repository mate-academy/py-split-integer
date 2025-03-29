from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    error_message = "Sum of parts should be equal to value."
    assert sum(split_integer(25, 5)) == 25, error_message


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    error_message = "Value should be split into equal parts"
    assert split_integer(10, 5) == [2, 2, 2, 2, 2], error_message


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    error_message = "Parts should be equal to value when split into one part."
    assert split_integer(8, 1) == [8], error_message


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    error_message = "Parts should be sorted when not all parts are equal."
    assert split_integer(5, 4) == [1, 1, 1, 2], error_message


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    error_message = "Zeros should be added when value < than number of parts."
    assert split_integer(3, 4) == [0, 1, 1, 1], error_message
