from app.split_integer import split_integer


def test_split_integer_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_even_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_multiple_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_large_value() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_edge_case() -> None:
    assert split_integer(10, 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_split_integer_large_parts() -> None:
    assert split_integer(110, 10) == [11] * 10
