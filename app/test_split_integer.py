from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    split = split_integer(2, 2)
    assert split == [1, 1]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    split = split_integer(12, 6)
    assert split == [2, 2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    split = split_integer(1, 1)
    assert split == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(12, 5)
    assert result == sorted(split_integer(12, 5))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    split = split_integer(4, 8)
    assert split == [0, 0, 0, 0, 1, 1, 1, 1]
