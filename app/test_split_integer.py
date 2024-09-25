from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(42, 5)) == 42
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(10, 5) == [2, 2, 2, 2, 2]
    ), ("Should split the value into equal parts when it is divisible "
        "by the number of parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(6, 1) == [6]
    ), "Should return single part equal to the value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(10, 4) == [2, 2, 3, 3]
    ), "Parts should be sorted from smallest to largest"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 5) == [0, 0, 0, 1, 1]
    ), "Should add zeros when the value is less than the number of parts"
