from app.split_integer import split_integer


def test_single_part_returns_whole_value() -> None:
    assert split_integer(8, 1) == [8]


def test_even_split_into_two_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_uneven_split_into_four_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_into_six_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_value_smaller_than_parts() -> None:
    result = split_integer(3, 5)
    assert len(result) == 5
    assert sum(result) == 3
    assert max(result) - min(result) <= 1
    assert result == sorted(result)


def test_large_value_large_parts() -> None:
    result = split_integer(100, 10)
    assert len(result) == 10
    assert sum(result) == 100
    assert max(result) - min(result) <= 1
    assert result == sorted(result)


def test_difference_between_max_and_min_is_at_most_one() -> None:
    result = split_integer(25, 4)
    assert max(result) - min(result) <= 1


def test_array_is_sorted() -> None:
    result = split_integer(19, 5)
    assert result == sorted(result)
