from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 20
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    expected_part = value // number_of_parts
    assert all(part == expected_part for part in result), ("All parts"
                                                           " must be equal")
    assert len(result) == number_of_parts, ("Sum parts should"
                                            " be equal to number_of_parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 6
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert len(result) == 1, "List must be equal to one"
    assert result[0] == value, "Element must equal to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 8
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == sorted(result), ("Parts should be sorted when they are "
                                      "not equal")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts
    assert sum(result) == value
    assert all(part in [0, 1] for part in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
