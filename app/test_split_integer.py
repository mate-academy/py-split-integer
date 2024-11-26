from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 12
    number_of_parts = 5
    result_split_integer = split_integer(value, number_of_parts)
    assert sum(result_split_integer) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 4
    result_split_integer = split_integer(value, number_of_parts)
    if value % number_of_parts == 0:
        assert all(part == value // number_of_parts
                   for part in result_split_integer)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 12
    number_of_parts = 1
    result_split_integer = split_integer(value, number_of_parts)
    assert len(result_split_integer) == 1
    assert result_split_integer[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 12
    number_of_parts = 4
    result_split_integer = split_integer(value, number_of_parts)
    assert result_split_integer == sorted(result_split_integer)
    assert max(result_split_integer) - min(result_split_integer) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 12
    number_of_parts = 20
    result_split_integer = split_integer(value, number_of_parts)
    zeros_count = result_split_integer.count(0)
    if value < number_of_parts:
        assert zeros_count == number_of_parts - value
    else:
        assert zeros_count == 0
