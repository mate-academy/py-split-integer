from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(4, 6) == [0, 0, 1, 1, 1, 1]


def test_parts_difference_should_be_less_or_equal_one() -> None:
    result = split_integer(123, 17)
    assert max(result) - min(result) <= 1


def test_remainder_should_be_added_to_first_elements() -> None:
    result = split_integer(8, 3)
    assert result == [2, 3, 3]