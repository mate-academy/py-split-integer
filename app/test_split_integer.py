from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(17, 4)
    assert parts == [4, 4, 4, 5]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(10, 5)
    assert parts == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(13, 1)
    assert parts == [13]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(19, 5)
    assert parts == [3, 4, 4, 4, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(3, 8)
    print(parts)
    assert parts == [0, 0, 0, 0, 0, 1, 1, 1]
