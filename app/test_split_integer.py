from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 20
    number_of_parts = 3

    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 21
    number_of_parts = 3

    result = split_integer(value, number_of_parts)

    if value % number_of_parts:
        assert (max(result) - min(result)) == 1
    else:
        assert (max(result) - min(result)) == 0


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 20
    number_of_parts = 1

    result = split_integer(value, number_of_parts)

    assert result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 20
    number_of_parts = 3

    result = split_integer(value, number_of_parts)
    sorted_result = sorted(result)
    assert result == sorted_result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 8

    result = split_integer(value, number_of_parts)

    assert result == [0, 0, 0, 1, 1, 1, 1, 1]
