from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(32, 6)
    assert sum(parts) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(36, 6)
    assert min(parts) == max(parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(9, 1)
    assert parts[0] == 9


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4)
    assert sorted(parts) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(3, 6)
    assert parts == [0, 0, 0, 1, 1, 1]
