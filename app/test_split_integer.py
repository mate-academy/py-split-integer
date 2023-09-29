from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(42, 3)) == 42


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(42, 7)
    assert all(part == parts[0] for part in parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(42, 1) == [42]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(42, 4) == sorted(split_integer(42, 4))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2) == [0, 1]
