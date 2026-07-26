from app.split_integer import split_integer


def test_correct_number_of_parts() -> None:
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(1, 1)) == 1
    assert len(split_integer(100, 10)) == 10


def test_sum_equals_value() -> None:
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(1, 1)) == 1
    assert sum(split_integer(99, 10)) == 99


def test_parts_difference_at_most_one() -> None:
    for value, parts in [(10, 3), (1, 1), (99, 10), (15, 7), (100, 33)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_parts_are_sorted() -> None:
    result = split_integer(10, 3)
    assert result == sorted(result)


def test_all_parts_equal_when_divisible() -> None:
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3]


def test_unequal_split_distributes_evenly() -> None:
    result = split_integer(10, 3)
    assert sorted(result) == result
    assert max(result) - min(result) <= 1
    assert sum(result) == 10
    assert len(result) == 3


def test_not_just_last_incremented() -> None:
    result = split_integer(7, 3)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_split_integer_for_various_cases() -> None:
    test_cases = [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
    for value, parts, expected in test_cases:
        result = split_integer(value, parts)
        assert result == expected
