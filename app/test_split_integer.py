from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32, \
        "Sum of the output array should be equal to input value!"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4], \
        ("If value is divisible by parts, we should have "
         "an array consist of equal numbers!")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17], \
        "Output should be equal to value!"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], \
        "Output should be sorted!"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 6) == [0, 0, 0, 1, 1, 1], \
        ("If amount of parts is more than possible, "
         "your result should contain zeros!")
