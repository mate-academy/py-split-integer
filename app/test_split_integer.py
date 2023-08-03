from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 15
    number_of_parts = 5
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 25
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert all(x == result[0] for x in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 25
    number_of_parts = 1
    assert split_integer(value, number_of_parts) == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 30
    number_of_parts = 4
    assert (split_integer(value, number_of_parts)
            == sorted(split_integer(value, number_of_parts)))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 7
    number_of_parts = 10
    assert len(split_integer(value, number_of_parts)) == number_of_parts
    assert sum(split_integer(value, number_of_parts)) == value
