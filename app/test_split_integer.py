from app.split_integer import split_integer


def test_example_from_description() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_correct_number_of_elements() -> None:
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(100, 10)) == 10
    assert len(split_integer(2, 2)) == 2
    assert len(split_integer(11, 4)) == 4


def test_sorted_ascending() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))
    assert split_integer(32, 6) == sorted(split_integer(32, 6))
    assert split_integer(11, 4) == sorted(split_integer(11, 4))


def test_max_min_difference() -> None:
    cases = [(17, 4), (32, 6), (11, 4), (6, 2), (8, 3)]
    for value, parts in cases:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_sum_equals_value() -> None:
    cases = [(17, 4), (32, 6), (11, 4), (6, 2), (8, 3), (100, 9)]
    for value, parts in cases:
        assert sum(split_integer(value, parts)) == value
