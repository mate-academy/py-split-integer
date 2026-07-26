from app.split_integer import split_integer


def test_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_even_split() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_multiple_remainder_values() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_length() -> None:
    result = split_integer(20, 5)
    assert len(result) == 5


def test_sorted_result() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_difference_between_numbers() -> None:
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


def test_sum_equals_original_value() -> None:
    value = 25
    parts = 4
    result = split_integer(value, parts)
    assert sum(result) == value
