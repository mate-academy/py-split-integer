from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 5

    result = split_integer(value=value, number_of_parts=parts)

    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 15
    parts = 5
    element = value / parts

    result = split_integer(value=value, number_of_parts=parts)

    for el in result:
        assert el == element


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 15
    parts = 1

    result = split_integer(value=value, number_of_parts=parts)

    assert len(result) == parts and result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 27
    parts = 6

    result = split_integer(value=value, number_of_parts=parts)

    assert sorted(result) == result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 7
    parts = 11
    difference = parts - value

    result = split_integer(value=value, number_of_parts=parts)

    for value in result[:difference]:
        assert value == 0
