from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    num1, num2 = 20, 4
    result = split_integer(num1, num2)
    assert sum(result) == num1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    num1, num2 = 12, 3
    result = split_integer(num1, num2)
    assert result == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    num1, num2 = 20, 1
    result = split_integer(num1, num2)
    assert result[0] == num1
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    num1, num2 = 21, 4
    result = split_integer(num1, num2)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    num1, num2 = 3, 5
    result = split_integer(num1, num2)
    assert result == [0, 0, 1, 1, 1]


def test_difference_of_the_parts_should_be_equal_or_less_than_one() -> None:
    num1, num2 = 20, 3
    result = split_integer(num1, num2)
    assert max(result) - min(result) <= 1


def test_if_parts_are_sorted_ascending_order() -> None:
    num1, num2 = 13, 2
    result = split_integer(num1, num2)
    assert result == sorted(result)
