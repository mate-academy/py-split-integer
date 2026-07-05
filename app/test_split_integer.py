from app.split_integer import split_integer


def test_split_integer_value_divided_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_value_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_length() -> None:
    assert len(split_integer(32, 6)) == 6


def test_split_integer_sorted() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_split_integer_sum() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_split_integer_max_min_difference() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(10, 3) == [3, 3, 4]


def test_split_integer_max_min_difference_length() -> None:
    assert split_integer(7, 3) == [2, 2, 3]


def test_split_integer_distributes_remainder_evenly() -> None:
    """Test that remainder is distributed across
     multiple parts, not just added to last."""
    assert split_integer(5, 3) == [1, 2, 2]


def test_split_integer_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_value_less_than_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
