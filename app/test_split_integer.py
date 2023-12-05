from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(6, 3)
    assert result == [2, 2, 2]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(16, 4)
    assert result == [4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(7, 1)
    assert result == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 7)
    print(result)
    assert result == [2, 2, 2, 2, 3, 3, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]
