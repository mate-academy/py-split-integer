from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value=value, number_of_parts=number_of_parts)
    assert sum(parts) == value
    assert len(parts) == number_of_parts
    assert parts == sorted(parts)
    assert max(parts) - min(parts) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    parts = split_integer(value=value, number_of_parts=number_of_parts)
    expected = value // number_of_parts
    assert sum(parts) == value
    assert len(parts) == number_of_parts
    assert parts == sorted(parts)
    assert parts == [expected] * number_of_parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value=value, number_of_parts=number_of_parts)
    assert parts == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 19
    number_of_parts = 4
    parts = split_integer(value=value, number_of_parts=number_of_parts)
    remainder = value % number_of_parts
    assert parts == sorted(parts)
    assert max(parts) - min(parts) <= 1
    assert sum(1 for p in parts if p == max(parts)) == remainder


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    number_of_parts = 4
    parts = split_integer(value=value, number_of_parts=number_of_parts)
    assert len(parts) == number_of_parts
    assert max(parts) - min(parts) <= 1
    assert sum(parts) == value
