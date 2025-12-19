from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(10, 2)
    assert sum(parts) == 10

def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(20, 3)
    assert max(parts) - min(parts) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(10, 1)
    assert parts[0] == sum(parts)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(10, 3)
    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(3, 4)
    assert parts.count(0) == 4 - 3

def test_parts_should_have_zeroes_when_value_is_zero() -> None:
    parts = split_integer(0, 4)
    assert sum(parts) == 0 and parts[0] == parts[1] == parts[2] == parts[3] and len(parts) == 4