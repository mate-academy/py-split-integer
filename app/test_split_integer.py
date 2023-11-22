from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(25, 5)) == 25


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(value=6, number_of_parts=2)
    assert all(part == 6 // 2 for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(value=17, number_of_parts=1) == [17]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    sort_part = split_integer(value=17, number_of_parts=4)
    assert sort_part == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    zero_part = split_integer(value=8, number_of_parts=12)
    assert zero_part[0] == 0
