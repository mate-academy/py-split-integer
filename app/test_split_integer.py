from app.split_integer import split_integer


def test_sum_of_parts_equals_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_parts_are_equal_if_value_divisible_by_number() -> None:
    result = split_integer(8, 2)
    assert result[0] == result[1]


def test_returns_value_if_number_is_one() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_are_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_add_zeros_when_value_is_less_than_number() -> None:
    result = split_integer(8, 12)
    assert result[0:4] == [0, 0, 0, 0]


def test_add_zeroes_if_value_is_negative_and_less_than_number() -> None:
    result = split_integer(-8, 12)
    assert result[-4:] == [0, 0, 0, 0]
