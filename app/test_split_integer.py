from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 2)) == 8, \
        "Sum of parts should be equal to the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(8, 2) == [4, 4], \
        "Value should be split into equal parts when divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10], \
        "Function should return the whole value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], \
        "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2) == [0, 1], \
        "Zeros should be added when the value is less than the number of parts"
