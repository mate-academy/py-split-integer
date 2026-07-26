from app import split_integer


def test_sum_of_parts_is_correct() -> None:
    result = split_integer.split_integer(17, 4)
    assert sum(result) == 17
    assert result == [4, 4, 4, 5]


def test_all_parts_are_equal_when_divisible() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_single_part_returns_value() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_parts_are_sorted_and_optimal() -> None:
    res = split_integer.split_integer(32, 6)
    assert res == [5, 5, 5, 5, 6, 6]
    assert res == sorted(res)


def test_result_contains_zeros_when_needed() -> None:
    assert split_integer.split_integer(2, 5) == [0, 0, 0, 1, 1]
