from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32, (
        "The parts returned by split_integer(32, 6) should sum to 32"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(6, 2)

    assert len(parts) == 2 and parts == [3, 3], (
        "The parts return by split_integer of (6, 2)"
        "should split into equal parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1)

    assert len(parts) == 1 and parts == [8], (
        "split_integer of (8, 1) should split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], (
        "The parts returned by split_integer(17, 4) should be sorted"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        "The function should add zerps when value es less than number of parts"
    )


def test_diff_between_max_and_min_should_be_less_or_equal_to_one() -> None:
    parts = split_integer(6, 2)

    assert max(parts) - min(parts) <= 1, (
        "The difference between max and min should be less or equal to one"
    )
