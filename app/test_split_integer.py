import app.split_integer as si


def test_single_part() -> None:
    assert si.split_integer(8, 1) == [8]


def test_evenly_divisible() -> None:
    assert si.split_integer(6, 2) == [3, 3]


def test_with_remainder() -> None:
    assert si.split_integer(17, 4) == [4, 4, 4, 5]


def test_large_numbers_with_remainder() -> None:
    assert si.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_value_equals_number_of_parts() -> None:
    assert si.split_integer(10, 10) == [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ]


def test_large_value_small_parts() -> None:
    assert si.split_integer(100, 3) == [33, 33, 34]


def test_minimal_positive_integers() -> None:
    assert si.split_integer(1, 1) == [1]


def test_remainder_distribution() -> None:
    assert si.split_integer(7, 3) == [2, 2, 3]


def test_multiple_remainders() -> None:
    assert si.split_integer(20, 7) == [2, 3, 3, 3, 3, 3, 3]


def test_very_large_value() -> None:
    assert si.split_integer(999, 10) == [
        99, 100, 100, 100, 100, 100, 100, 100, 100, 100
    ]


def test_two_parts_with_remainder() -> None:
    assert si.split_integer(11, 2) == [5, 6]


def test_three_parts_with_remainder() -> None:
    assert si.split_integer(14, 3) == [4, 5, 5]
