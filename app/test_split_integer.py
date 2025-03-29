from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(32, 6)) == 32
    ), "The sum of the parts should be equal to the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(25, 5) == [5, 5, 5, 5, 5]
    ), ("List should have equal parts if the original value "
        "is divisible by the number of parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(10, 1) == [10]
    ), ("If the number of parts is 1, "
        "the resulting list should contain the original value")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(18, 4) == sorted((split_integer(18, 4)))
    ), "Resulting list should be sorted when parts are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 4) == [0, 0, 1, 1]
    ), ("If the value is less than the number of parts, "
        "zeros must be added to match the number of parts")
