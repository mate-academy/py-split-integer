from app.split_integer import split_integer


def test_single_part_returns_full_value() -> None:
    assert split_integer(8, 1) == [8]


def test_even_split() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_large_split_with_remainder() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_zero_value_returns_zeros() -> None:
    assert split_integer(0, 3) == [0, 0, 0]


def test_more_parts_than_value() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]


def test_max_min_difference_is_not_more_than_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_result_is_sorted() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_length_equals_number_of_parts() -> None:
    result = split_integer(17, 4)
    assert len(result) == 4


def test_sum_equals_original_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17
