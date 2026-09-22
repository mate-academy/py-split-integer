from app import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    result = split_integer.split_integer(value, 4)

    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer.split_integer(6, 2)

    assert max(result) - min(result) == 0


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer.split_integer(6, 1)

    assert result == [6]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 10
    result = split_integer.split_integer(value, 4)

    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer.split_integer(2, 5)

    assert len(result) == 5
    assert result == sorted(result)
    assert min(result) == 0
    assert max(result) == 1
