from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(25, 4)) == 25
    ), "Sum of parts should be equal to 25"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(12, 3) == [4, 4, 4]
    ), "Parts should be equal when value is divisible by the number of parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(7, 1) == [7]
    ), "Should return [7] when number_of_parts is 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(19, 3) == [6, 6, 7]
    ), "Parts should be sorted in ascending order when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 5) == [0, 0, 0, 1, 1, 1]
    ), ("Should return a list with zeros "
        "and ones when value is less than number_of_parts")
