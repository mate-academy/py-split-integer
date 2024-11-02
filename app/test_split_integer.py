from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    parts = split_integer(value, number_of_parts)
    assert parts == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert parts == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


def test_max_min_difference_should_be_less_than_equal_to_one() -> None:
    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert max(parts) - min(parts) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert parts == [0, 0, 1, 1, 1]


def test_should_split_into_different_parts() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert parts in ([3, 3, 4], [4, 3, 3])


def test_should_split_on_incorrect_parts() -> None:
    value = 5
    number_of_parts = 2
    parts = split_integer(value, number_of_parts)
    assert parts in ([2, 3], [3, 2])
