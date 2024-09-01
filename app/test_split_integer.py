from app.split_integer import split_integer as si


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    parts = si(value, number_of_parts)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 2
    parts = si(value, number_of_parts)
    assert parts == [5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 10
    number_of_parts = 1
    parts = si(value, number_of_parts)
    assert parts == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 10
    number_of_parts = 3
    parts = si(value, number_of_parts)
    assert parts == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3
    parts = si(value, number_of_parts)
    assert parts == [0, 1, 1]
