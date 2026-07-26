from app.split_integer import split_integer


def test_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_divisible_cases() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_remainder_distribution() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(5, 3) == [1, 2, 2]
    assert split_integer(10, 4) == [2, 2, 3, 3]
    assert split_integer(17, 2) == [8, 9]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_edge_cases() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert split_integer(0, 3) == [0, 0, 0]


def test_general_properties() -> None:
    res = split_integer(17, 4)
    assert len(res) == 4
    assert sum(res) == 17
    assert res == sorted(res)
    assert max(res) - min(res) <= 1


def test_specific_small_and_edge_cases() -> None:
    assert split_integer(1, 2) == [0, 1]
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(4, 2) == [2, 2]
    assert split_integer(9, 3) == [3, 3, 3]
    assert split_integer(6, 4) == [1, 1, 2, 2]
    assert split_integer(7, 7) == [1, 1, 1, 1, 1, 1, 1]
