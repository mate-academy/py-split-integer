from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 4

    function_result = split_integer(value, parts)

    assert sum(function_result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    parts = 2

    function_result = split_integer(value, parts)

    assert function_result == [6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 3
    parts = 1

    function_result = split_integer(value, parts)

    assert function_result == [3]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 3
    parts = 2

    function_result = split_integer(value, parts)

    assert function_result == [1, 2]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    parts = 4

    function_result = split_integer(value, parts)

    assert function_result == [0, 1, 1, 1]
