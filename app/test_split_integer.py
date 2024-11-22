from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 60
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, ("returned sum of "
                                  "parts should be equal to value.")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 60
    number_of_parts = 6
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert result == [10, 10, 10, 10, 10, 10], ("If value is divisible by "
                                                "number of parts, function "
                                                "should return list of "
                                                "elements equal to "
                                                "value/number_of_parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 60
    number_of_parts = 1
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert result == [value], ("If number_of_parts is equal to 1, "
                               "function should return value.")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 50
    number_of_parts = 4
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert result == [12, 12, 13, 13], ("If parts are not equal, "
                                        "they should be sorted.")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 4
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert result == [0, 1, 1, 1], ("If value is less than number_of_parts, "
                                    "function should add 0 to array")
