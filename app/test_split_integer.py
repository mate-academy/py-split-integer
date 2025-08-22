from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    assert sum(result) == value and len(result) == number_of_parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 5
    check_obj = value // number_of_parts
    result = split_integer(value, number_of_parts)
    for parts in result:
        assert parts == check_obj
    assert len(result) == number_of_parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 14
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result[0] == value and len(result) == number_of_parts


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 20
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert (sorted(result) == result
            and len(result) == number_of_parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert 0 in result and len(result) == number_of_parts
