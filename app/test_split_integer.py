from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        split_integer(17, 4) == [4, 4, 4, 5]
    ), "Expected [4, 4, 4, 5] when splitting 17 into 4 part"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(6, 2) == [3, 3]
    ), "Expected [3, 3] when splitting 6 into 2 parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), "Expected [8] when splitting 8 into 1 part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Expected [8] when splitting 32 into 6 part"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 3) == [0, 0, 1]
    ), "Expected [0, 0, 1] when splitting 1 into 3 part"
