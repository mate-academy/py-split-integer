from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 8
    number_of_parts = 1

    assert sum(split_integer(value, number_of_parts)) == value

    value = 6
    number_of_parts = 2

    assert sum(split_integer(value, number_of_parts)) == value

    value = 17
    number_of_parts = 4

    assert sum(split_integer(value, number_of_parts)) == value

    value = 32
    number_of_parts = 6

    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 8
    number_of_parts = 1

    assert len(split_integer(value, number_of_parts)) == number_of_parts
    assert all(part == value // number_of_parts for part in split_integer(value, number_of_parts))

    value = 16
    number_of_parts = 2

    assert len(split_integer(value, number_of_parts)) == number_of_parts
    assert all(part == value // number_of_parts for part in split_integer(value, number_of_parts))


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1

    assert len(split_integer(value, number_of_parts)) == 1
    assert split_integer(value, number_of_parts)[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 8
    number_of_parts = 1

    assert split_integer(value, number_of_parts) == sorted(split_integer(value, number_of_parts))

    value = 6
    number_of_parts = 2

    assert split_integer(value, number_of_parts) == sorted(split_integer(value, number_of_parts))

    value = 17
    number_of_parts = 4

    assert split_integer(value, number_of_parts) == sorted(split_integer(value, number_of_parts))

    value = 32
    number_of_parts = 6

    assert split_integer(value, number_of_parts) == sorted(split_integer(value, number_of_parts))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4

    parts = split_integer(value, number_of_parts)

    assert len(parts) == number_of_parts

    for i in range(value):
        assert parts[i] == 0

    for i in range(value, number_of_parts):
        assert parts[i] != 0
