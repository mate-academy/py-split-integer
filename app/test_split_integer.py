from app.split_integer import split_integer


def test_split_integer_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_two_parts_equal() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_multiple_parts_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_larger_number() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_max_min_difference() -> None:
    result = split_integer(10, 3)
    assert max(result) - min(result) <= 1


def test_split_integer_sorted() -> None:
    result = split_integer(20, 6)
    assert result == sorted(result)


def test_split_integer_exact_division() -> None:
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3]