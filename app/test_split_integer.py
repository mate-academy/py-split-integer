from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)

    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 7007
    number_of_parts = 1001
    parts = split_integer(value, number_of_parts)

    assert (
            value % number_of_parts == 0
            and set(parts) == {value / number_of_parts}
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 10
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)

    assert int(parts) / value == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 15
    parts = split_integer(value, number_of_parts)

    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)

    assert parts[:-value] == (number_of_parts - value) * [0]
