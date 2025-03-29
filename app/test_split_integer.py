from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32, (
        "Sum of the function result with value {32} "
        "and number_of_parts {6} should be equal to {32}")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(16, 4) == [4, 4, 4, 4], (
        "Value should split into into equal parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "Result should be equal to value when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "Result list  should be sorted"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        "Result should contain zeros when value is less than number of parts"
    )
