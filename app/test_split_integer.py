from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)

    assert sum(result) == value

    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)

    assert sum(result) == value

    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)

    assert sum(result) == value

    value = 32
    number_of_parts = 6
    result = split_integer(value, number_of_parts)

    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert all(part == value // number_of_parts for part in result)

    value = 16
    number_of_parts = 2
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert all(part == value // number_of_parts for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)

    assert len(result) == 1
    assert result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)

    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)

    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)

    value = 32
    number_of_parts = 6
    result = split_integer(value, number_of_parts)

    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4

    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts

    for i in range(value):
        assert result[i] == 0

    for i in range(value, number_of_parts):
        assert result[i] != 0
