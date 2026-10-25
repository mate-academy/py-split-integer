from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 2)) == 10, \
        "Sum of all elements should be equal to 10"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], \
        "Result should be equal to [3, 3]"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], \
        "The result must contain only one value [8]"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], \
        "The result must be sorted from the smallest element to the largest."


def test_split_integer_32_into_6_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
