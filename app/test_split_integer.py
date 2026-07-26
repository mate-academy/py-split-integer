from app.split_integer import split_integer


def test_return_single_part_when_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_equal_parts_when_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_difference_between_max_and_min_less_or_equal_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_array_is_sorted_ascending() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_correct_number_of_parts_returned() -> None:
    parts = split_integer(10, 3)
    assert len(parts) == 3


def test_sum_of_parts_equals_value() -> None:
    value = 123
    parts_count = 17
    parts = split_integer(value, parts_count)
    assert sum(parts) == value


def test_parts_difference_and_order_for_non_divisible() -> None:
    parts = split_integer(8, 3)
    assert max(parts) - min(parts) <= 1
    assert parts == sorted(parts)


def test_all_parts_are_integers() -> None:
    parts = split_integer(50, 7)
    assert all(isinstance(p, int) for p in parts)


def test_zero_values_when_value_less_than_parts() -> None:
    parts = split_integer(4, 6)
    # The array should contain zeros and be sorted ascending
    assert len(parts) == 6
    assert parts == sorted(parts)
    assert sum(parts) == 4
