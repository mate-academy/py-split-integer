from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(5, 1)) == 5
    ), "(5, 1) should return 5"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(36, 6) == [6, 6, 6, 6, 6, 6]
    ), "(36, 6) should return [6, 6, 6, 6, 6, 6]"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(11, 1) == [11]
    ), "(11, 1) should return [11]"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(13, 3) == [4, 4, 5]
    ), "(13, 3) should return [4, 4, 5]"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 5) == [0, 0, 0, 1, 1]
    ), "(2, 5) should return [0, 0, 0, 1, 1]"
