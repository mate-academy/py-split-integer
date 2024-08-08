from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32, (
        "Sum of the parts should be equal to the value."
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(30, 5) == [6, 6, 6, 6, 6], (
        "Should split into equal parts when value is divisible by parts."
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(20, 1) == [20], (
        "Should return part equal to value when split into one part."
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "Parts should be sorted when they are not equal."
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        "Should add zeros when value is less than number of parts."
    )
