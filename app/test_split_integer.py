from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 2
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 2
    expected = [5, 5]
    assert split_integer(value, number_of_parts) == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 4
    number_of_parts = 1
    expected = [4]
    assert split_integer(value, number_of_parts) == expected


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    expected = [4, 4, 4, 5]
    assert split_integer(value, number_of_parts) == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 6
    expected = [0, 1, 1, 1, 1, 1]
    assert split_integer(value, number_of_parts) == expected


def test_the_difference_of_the_max_and_min_numbers() -> None:
    value = 5
    number_of_parts = 2
    assert (max(split_integer(value, number_of_parts))
            - min(split_integer(value, number_of_parts))
            <= 1)
