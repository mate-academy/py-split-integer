from app.split_integer import split_integer


def test_split_integer_value_divided_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3]


def test_split_integer_value_with_remainder() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]


def test_split_integer_length() -> None:
    value, parts = 32, 6
    result = split_integer(value, parts)
    assert len(result) == parts


def test_split_integer_sorted() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert result == sorted(result)


def test_split_integer_sum() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value


def test_split_integer_max_min_difference() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert max(result) - min(result) <= 1


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 3)
    assert result == [4, 3, 3]


def test_split_integer_max_min_difference_length() -> None:
    result = split_integer(7, 3)
    assert result == [3, 2, 2]
