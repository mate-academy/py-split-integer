from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 2
    parts = split_integer(value, number_of_parts)
    assert len(set(parts)) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 7
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert len(parts) == 1
    assert parts[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(10, 4)
    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 8
    parts = split_integer(value, number_of_parts)
    assert len(parts) == number_of_parts
    assert sum(parts) == value
    assert 0 in parts
