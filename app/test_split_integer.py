from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(8, 1)
    assert sum(parts) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(6, 2)
    assert all(x == parts[0] for x in parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 10
    parts = split_integer(10, 1)
    assert len(parts) == 1
    assert parts[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(32, 6)
    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    parts = split_integer(3, 5)
    assert sum(parts) == value
    assert len(parts) == number_of_parts
    assert 0 in parts
