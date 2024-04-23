from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    split = split_integer(value=20, number_of_parts=3)
    assert split == [6, 7, 7]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    split = split_integer(value=16, number_of_parts=4)
    assert split == [4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    split = split_integer(value=20, number_of_parts=1)
    assert split == [20]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    split = split_integer(value=17, number_of_parts=4)
    assert split == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    split = split_integer(value=2, number_of_parts=5)
    assert (split == [0, 0, 0, 1, 1])
