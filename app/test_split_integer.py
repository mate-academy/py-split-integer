from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(57, 13)
    assert sum(parts) == 57


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(100, 10)
    assert max(parts) == min(parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(42, 1)
    assert parts[0] == 42


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(10, 3)
    assert parts[len(parts) - 1] - parts[0] <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(1, 3)
    assert 0 in parts
