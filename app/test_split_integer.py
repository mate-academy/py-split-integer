from app.split_integer import split_integer


def test_split_integer_basic_cases() -> None:
    cases = [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]

    for value, parts, expected in cases:
        assert list(split_integer(value, parts)) == expected


def test_split_integer_equal_parts() -> None:
    cases = [
        (6, 2, [3, 3]),
        (8, 4, [2, 2, 2, 2]),
        (10, 5, [2, 2, 2, 2, 2]),
    ]

    for value, parts, expected in cases:
        assert list(split_integer(value, parts)) == expected


def test_split_integer_with_remainder() -> None:
    cases = [
        (8, 3, [2, 3, 3]),
        (6, 4, [1, 1, 2, 2]),
        (17, 4, [4, 4, 4, 5]),
        (32, 5, [6, 6, 6, 7, 7]),
    ]

    for value, parts, expected in cases:
        assert list(split_integer(value, parts)) == expected


def test_split_integer_with_zeros() -> None:
    cases = [
        (2, 3, [0, 1, 1]),
        (6, 8, [0, 0, 1, 1, 1, 1, 1, 1]),
        (1, 3, [0, 0, 1]),
    ]

    for value, parts, expected in cases:
        assert list(split_integer(value, parts)) == expected
