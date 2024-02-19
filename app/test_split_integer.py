from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    array_of_elements = split_integer(15, 6)
    assert sum(array_of_elements) == 15


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    array_of_elements = split_integer(6, 2)
    assert array_of_elements == [6 / 2] * 2


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    array_of_elements = split_integer(8, 1)
    assert array_of_elements[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    array_of_elements = split_integer(17, 4)
    assert array_of_elements == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    array_of_elements = split_integer(3, 5)
    assert array_of_elements == [0, 0, 1, 1, 1]
