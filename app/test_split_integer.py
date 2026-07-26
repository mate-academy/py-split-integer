from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    expected_value = [4, 4, 4, 5]
    assert split_integer(17, 4) == expected_value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected_value = [6, 6, 6, 6, 6, 6]
    assert split_integer(36, 6) == expected_value


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    expected_value = [7]
    assert split_integer(7, 1) == expected_value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    expected_value = [5, 5, 5, 6]
    assert split_integer(21, 4) == expected_value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    expected_value = [0, 0, 1, 1, 1]
    assert split_integer(3, 5) == expected_value
