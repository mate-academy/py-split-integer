from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        f"sum of {split_integer(32, 6)} does not equal 32"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], (
        f"number of parts in {split_integer(6, 2)} does not equal 2"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        f"parts in {split_integer(8, 1)} does not equal [8]"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        f"parts in {split_integer(32, 6)} are not sorted"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(4, 8) == [0, 0, 0, 0, 1, 1, 1, 1], (
        f"zeros not added in {split_integer(4, 8)} as value is less than parts"
    )
