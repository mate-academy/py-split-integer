from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(20, 4)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(20, 1) == 20
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(21, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_difference_of_the_parts_should_be_equal_or_less_than_one() -> None:
    result = split_integer(20, 3)
    assert max(result) - min(result) <= 1


def test_if_parts_are_sorted_ascending_order() -> None:
    result = split_integer(13, 2)
    assert split_integer(13, 2) == sorted(result)
