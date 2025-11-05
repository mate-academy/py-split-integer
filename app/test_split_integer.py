from app.split_integer import split_integer


def test_sum_of_parts_equals_original_value() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value

    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value

    value = 0
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


def test_equal_parts_when_value_divisible() -> None:
    value = 12
    number_of_parts = 4
    expected = [3, 3, 3, 3]
    result = split_integer(value, number_of_parts)
    assert result == expected


def test_single_part_equals_value() -> None:
    value = 8
    number_of_parts = 1
    expected = [8]
    result = split_integer(value, number_of_parts)
    assert result == expected


def test_parts_are_sorted_and_difference_is_at_most_one() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)
    assert max(parts) - min(parts) <= 1

    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)
    assert max(parts) - min(parts) <= 1


def test_zeros_are_added_when_value_is_less_than_parts() -> None:
    value = 3
    number_of_parts = 5
    expected = [0, 0, 1, 1, 1]
    result = split_integer(value, number_of_parts)
    assert result == expected

    value = 0
    number_of_parts = 4
    expected = [0, 0, 0, 0]
    result = split_integer(value, number_of_parts)
    assert result == expected
