from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6

    split_integer_output = split_integer(value=value,
                                         number_of_parts=number_of_parts)

    assert sum(split_integer_output) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2

    split_integer_output = split_integer(value=value,
                                         number_of_parts=number_of_parts)

    assert split_integer_output == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1

    assert split_integer(value=value, number_of_parts=number_of_parts) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4

    split_integer_output = split_integer(value=value,
                                         number_of_parts=number_of_parts)

    assert sorted(split_integer_output) == split_integer_output


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5

    split_integer_output = split_integer(value=value,
                                         number_of_parts=number_of_parts)

    assert split_integer_output.count(0) == number_of_parts - value
