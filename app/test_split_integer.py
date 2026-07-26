from app.split_integer import split_integer


def test_one_part():
    assert split_integer(8, 1) == [8]


def test_equal_split():
    assert split_integer(6, 2) == [3, 3]


def test_not_divisible():
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_bigger_split():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_sorted_result():
    result = split_integer(20, 6)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
