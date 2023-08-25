from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = sum(split_integer(32, 6))
    expected = 32
    assert result == expected, f"{result} should be equal to {expected}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 3)
    assert result[0] == result[1] == result[2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(2, 1)
    assert result[0] == 2, f"{result} should be equal to 2"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(13, 3)
    assert result == [4, 4, 5], f"{result} should be equal to [5, 4, 4]"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 3)
    assert result == [0, 1, 1], f"{result} should be equal to [1, 1, 0]"
