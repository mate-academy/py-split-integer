import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (10, 5, [2, 2, 2, 2, 2]),
])
def test_split_integer_equal_parts(value: int,
                                   number_of_parts: int,
                                   expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (20, 3, [6, 7, 7]),
])
def test_split_integer_unequal_parts(value: int,
                                     number_of_parts: int,
                                     expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (100, 10, [10] * 10),
    (101, 10, [10] * 9 + [11]),
    (1000, 3, [333, 333, 334]),
])
def test_split_integer_large_numbers(value: int,
                                     number_of_parts: int,
                                     expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (1, 1, [1]),
    (2, 2, [1, 1]),
    (3, 2, [1, 2]),
])
def test_split_integer_edge_cases(value: int,
                                  number_of_parts: int,
                                  expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (100, 50, [2] * 50),
    (101, 50, [2] * 49 + [3]),
    (1000, 100, [10] * 100),
])
def test_split_integer_large_number_of_parts(value: int,
                                             number_of_parts: int,
                                             expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (5, 1, [5]),
    (10, 1, [10]),
    (100, 1, [100]),
])
def test_split_integer_single_part(value: int,
                                   number_of_parts: int,
                                   expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (9, 3, [3, 3, 3]),
    (12, 4, [3, 3, 3, 3]),
    (15, 5, [3, 3, 3, 3, 3]),
])
def test_split_integer_exact_division(value: int,
                                      number_of_parts: int,
                                      expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (10, 3, [3, 3, 4]),
    (11, 3, [3, 4, 4]),
    (13, 4, [3, 3, 3, 4]),
])
def test_split_integer_remainder(value: int,
                                 number_of_parts: int,
                                 expected: list[int]) -> None:
    assert split_integer(value, number_of_parts) == expected
