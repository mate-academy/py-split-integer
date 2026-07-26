from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6
    expected_value = [5, 5, 5, 5, 6, 6]
    assert split_integer(value, number_of_parts) == expected_value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    expected_value = [3, 3]
    assert split_integer(value, number_of_parts) == expected_value


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    expected_value = [8]
    assert split_integer(value, number_of_parts) == expected_value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    expected_value = [4, 4, 4, 5]
    assert split_integer(value, number_of_parts) == expected_value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 6
    expected_value = [0, 0, 0, 0, 1, 1]
    assert split_integer(value, number_of_parts) == expected_value
