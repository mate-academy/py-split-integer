from app.split_integer import split_integer


def test_split_integer_returns_correct_value_for_8_and_1() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_returns_correct_value_for_6_and_2() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_returns_correct_value_for_17_and_4() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_returns_correct_value_for_32_and_6() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_returns_correct_number_of_parts() -> None:
    result = split_integer(10, 3)
    assert len(result) == 3


def test_split_integer_returns_sorted_array() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_split_integer_max_min_difference() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_split_integer_sum_equals_value() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value
