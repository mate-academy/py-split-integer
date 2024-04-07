from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value
    assert all(parts[i] <= parts[i + 1] for i in range(len(parts) - 1))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert len(parts) == number_of_parts
    assert max(parts) - min(parts) <= 1
    assert sorted(parts) == parts
    assert all(parts[i] <= parts[i + 1] for i in range(len(parts) - 1))


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert parts == [value]
    assert all(parts[i] <= parts[i + 1] for i in range(len(parts) - 1))


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sorted(parts) == parts
    assert all(parts[i] <= parts[i + 1] for i in range(len(parts) - 1))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 6
    number_of_parts = 8
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value
    assert len(parts) == number_of_parts
    assert max(parts) - min(parts) <= 1
    assert sorted(parts) == parts
    assert parts.count(0) == number_of_parts - value
    assert all(parts[i] <= parts[i + 1] for i in range(len(parts) - 1))
