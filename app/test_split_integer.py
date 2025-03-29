from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(6, 2)) == 6, (
        "Sum of the parts should equal the original value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(25, 5) == [5, 5, 5, 5, 5], (
        "Value should split into equal parts when divisible"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(29, 1) == [29], (
        "Splitting into one part should return the original value"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(13, 3) == [4, 4, 5], (
        "Parts should be sorted when they are not equal"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(4, 5) == [0, 1, 1, 1, 1], (
        "Zeros should be added when value is less than number of parts"
    )
