from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(17, 4)) == 17
    ), "Sum of split parts doesn't equal to given value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(9, 3) == [3, 3, 3]
    ), "Value should be split into equal parts (9 / 3 = 3 + 3 + 3)"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), "Return should be equal to 8 value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Parts should be sorted when they are not equal to each other"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 5) == [0, 0, 0, 1, 1]
    ), ("Function should add zeros to the beginning "
        "if given value is less than number of parts")
