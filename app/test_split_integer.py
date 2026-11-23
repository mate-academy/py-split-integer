from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(8, 3)) == 8
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(12, 3) == [4, 4, 4]
    ), "Value should splits into equal parts if it's divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(15, 1) == [15]
    ), "Functions should return value when it's only pne part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(14, 4) == [3, 3, 4, 4]
    ), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 5) == [0, 0, 1, 1, 1]
    ), "Function should add zeros when it's less than number of parts"
