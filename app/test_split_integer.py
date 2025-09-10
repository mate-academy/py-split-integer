import pytest
from app.split_integer import split_integer


def test_split_integer_single_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(1, 1) == [1]
    assert split_integer(100, 1) == [100]


def test_split_integer_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(9, 3) == [3, 3, 3]
    assert split_integer(20, 4) == [5, 5, 5, 5]
    assert split_integer(12, 6) == [2, 2, 2, 2, 2, 2]


def test_split_integer_unequal_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(7, 3) == [2, 2, 3]


def test_split_integer_more_parts_than_value() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
    assert split_integer(1, 3) == [0, 0, 1]


def test_split_integer_large_numbers() -> None:
    result = split_integer(1000, 7)
    assert len(result) == 7
    assert sum(result) == 1000
    assert max(result) - min(result) <= 1
    assert result == sorted(result)


def test_split_integer_result_length() -> None:
    assert len(split_integer(15, 4)) == 4
    assert len(split_integer(100, 7)) == 7
    assert len(split_integer(1, 10)) == 10


def test_split_integer_result_sum() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(100, 13)) == 100


def test_split_integer_result_sorted() -> None:
    result1 = split_integer(17, 4)
    assert result1 == sorted(result1)
    result2 = split_integer(32, 6)
    assert result2 == sorted(result2)
    result3 = split_integer(23, 7)
    assert result3 == sorted(result3)


def test_split_integer_max_min_difference() -> None:
    result1 = split_integer(17, 4)
    assert max(result1) - min(result1) <= 1
    result2 = split_integer(32, 6)
    assert max(result2) - min(result2) <= 1
    result3 = split_integer(23, 7)
    assert max(result3) - min(result3) <= 1
    result4 = split_integer(3, 5)
    assert max(result4) - min(result4) <= 1


def test_split_integer_edge_cases() -> None:
    assert split_integer(1, 2) == [0, 1]
    assert split_integer(2, 3) == [0, 1, 1]
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]
    assert split_integer(3, 3) == [1, 1, 1]


@pytest.mark.parametrize("value, parts, expected", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (10, 3, [3, 3, 4]),
    (7, 3, [2, 2, 3]),
    (3, 5, [0, 0, 1, 1, 1]),
])
def test_examples(value: int, parts: int, expected: list[int]) -> None:
    assert split_integer(value, parts) == expected
