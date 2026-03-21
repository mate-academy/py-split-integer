from app.split_integer import split_integer


def test_sum_or_parts_is_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_difference_between_maximum_and_minimum_value_is_less_or_equal_to_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1

    result_large = split_integer(100, 3)
    assert max(result_large) - min(result_large) <= 1


def test_ratio_is_maintained() -> None:
    assert len(split_integer(8, 1)) == 1
    assert len(split_integer(20, 5)) == 5


def test_parts_are_sorted_as_ascending() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_returns_equal_parts_when_value_is_divisible_by_number_of_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
