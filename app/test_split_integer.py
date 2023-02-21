from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(6, 2)) == 6,
        "Sum of all parts should be equal to 'value'"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(9, 3) == [3, 3, 3],
        "All values should be equal"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8],
        "The list should contain only one number"
        "which equal to 'value'"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == sorted(split_integer(32, 6)),
        "The list should be sorted by ascending"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 3) == [0, 1, 1],
        "A zero should be added if 'number_of_parts' "
        "is greater than the 'value'"
    )
