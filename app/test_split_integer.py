from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(3, 1)) == 3
    assert sum(split_integer(10, 4)) == 10
    assert sum(split_integer(20, 5)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]
    assert split_integer(12, 2) == [6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(4, 8) == [0, 0, 0, 0, 1, 1, 1, 1]
