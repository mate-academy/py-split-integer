from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
            sum(split_integer(8, 1)) == 8
    ), "Sum of the parts should be 8"
    assert (
            sum(split_integer(6, 2)) == 6
    ), "Sum of the parts should be 6"
    assert (
        sum(split_integer(17, 4)) == 17
    ), "Sum of the parts should be 17"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(10, 2) == [5, 5]
    ), "Should split 10 into [5, 5]"
    assert (
        split_integer(20, 4) == [5, 5, 5, 5]
    ), "Should split 20 into [5, 5, 5, 5]"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
            split_integer(10, 1) == [10]
    ), "Should split 10 into [10]"
    assert (
            split_integer(678, 1) == [678]
    ), "Should split 678 into [678]"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
            split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Should split 32 into [5, 5, 5, 5, 6, 6]"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
            split_integer(5, 6) == [0, 1, 1, 1, 1, 1]
    ), "Should split 5 into [0, 1, 1, 1, 1, 1]"
    assert (
            split_integer(10, 12) == [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ), "Should split 10 into [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"
