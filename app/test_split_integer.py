from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(17, 4)) == 17
    ), "The sum of the parts should be equal to the original value."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(9, 3) == [3, 3, 3]
    ), ("The value should be split into equal parts "
        "when it is divisible by the number of parts.")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(5, 1) == [5]
    ), ("When splitting into one part, "
        "the part should be equal to the original value.")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(20, 3) == [6, 7, 7]
    ), "The parts should be sorted in ascending order when they are not equal."


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 4) == [0, 0, 1, 1]
    ), "Zeros should be added when the value is less than the number of parts."
