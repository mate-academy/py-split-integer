from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = split_integer(10, 3)
    assert sum(value) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = split_integer(12, 3)
    assert len(set(value)) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = split_integer(12, 1)
    assert value == [12]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = split_integer(10, 3)
    assert sorted(value) == value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = split_integer(2, 5)
    assert value == [0, 0, 0, 1, 1]
