from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    sum_equal = split_integer(12, 25)

    assert sum(sum_equal) == 12


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    sum_equal = split_integer(12, 3)

    assert len(sum_equal) == 3


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    one_part = split_integer(12, 1)

    assert one_part == [12]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    one_part = split_integer(21, 8)

    assert one_part == [2, 2, 2, 3, 3, 3, 3, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    one_part = split_integer(0, 3)

    assert one_part == [0, 0, 0]
