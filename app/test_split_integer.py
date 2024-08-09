from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, (
        "The sum of the parts should be equal to the value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(25, 5) == [5, 5, 5, 5, 5], (
        "All the elements in the result should be equal when the value is "
        "divisible by parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10], (
        "The result should be equal to the value when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (split_integer(32, 6)
            == sorted(split_integer(32, 6))), (
        "The parts should be sorted when they are not equal"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(4, 7) == [0, 0, 0, 1, 1, 1, 1], (
        "Zeroes should be added when value is less than number of parts"
    )
