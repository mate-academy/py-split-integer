from app.split_integer import split_integer


def test_all_element_in_list_should_be_equal_to_value() -> None:
    result = split_integer(15, 3)
    assert (
        sum(result) == 15
    ), "Sum of numbers in list should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(6, 2) == [3, 3]
    ), "Equal parts if the value is divided by the number of parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(100, 1) == [100]
    ), "Part must be equal to value if number of parts == 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "If parts are not the same, list should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ), "If value is less than number, add zero to the start"
