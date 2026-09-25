from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    new_result = split_integer(12, 4)
    assert new_result == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    number = split_integer(8, 1)
    assert number == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    new_number = split_integer(17, 4)
    assert new_number == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    numbers = split_integer(2, 5)
    assert numbers == [0, 0, 0, 1, 1]
