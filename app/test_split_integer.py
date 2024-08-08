from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 3)) == 8, (
        "Sum of parts of 8 split into 3 parts should be 8"
    )
    assert sum(split_integer(17, 4)) == 17, (
        "Sum of parts of 17 split into 4 parts should be 17"
    )
    assert sum(split_integer(32, 6)) == 32, (
        "Sum of parts of 32 split into 6 parts should be 32"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], (
        "6 split into 2 parts should be [3, 3]"
    )
    assert split_integer(10, 5) == [2, 2, 2, 2, 2], (
        "10 split into 5 parts should be [2, 2, 2, 2, 2]"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "8 split into 1 part should be [8]"
    )
    assert split_integer(15, 1) == [15], (
        "15 split into 1 part should be [15]"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], (
        "17 split into 4 parts should be [4, 4, 4, 5]"
    )
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "32 split into 6 parts should be [5, 5, 5, 5, 6, 6]"
    )


def test_should_handle_values_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        "3 split into 5 parts should be [0, 0, 1, 1, 1]"
    )
    assert split_integer(2, 3) == [0, 1, 1], (
        "2 split into 3 parts should be [0, 1, 1]"
    )
