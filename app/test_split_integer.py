from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        split_integer(8, 4) == [2, 2, 2, 2]
    ), "sum of the parts should be equal to 8"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(6, 3) == [2, 2, 2]
    ), "should split 6 into 3 equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(12, 1) == [12]
    ), "should return part equal to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(13, 3) == [4, 4, 5]
    ), "result should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(0, 5) == [0, 0, 0, 0, 0]
    ), "should return zeros when value less than number of parts"


def test_should_increment_only_last_number() -> None:
    assert (
        split_integer(11, 3) == [3, 4, 4]
    ), "only last number should be incremented"
