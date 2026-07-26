from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 25
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value
    assert len(result) == number_of_parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]
    assert sum(result) == 3
    assert len(result) == 5
