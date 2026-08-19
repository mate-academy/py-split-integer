from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4

    result = split_integer(value, number_of_parts)

    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 32
    number_of_parts = 4
    expected_result = [8, 8, 8, 8]
    result = split_integer(value, number_of_parts)
    assert result == expected_result


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(32, 1) == [32]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(26, 3) == [8, 9, 9]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(7, 10) == [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
