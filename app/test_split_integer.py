from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_result = split_integer(17, 4)
    assert sum(test_result) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_result = split_integer(12, 2)
    assert test_result == [6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_result = split_integer(9, 1)
    assert test_result == [9]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_result = split_integer(32, 6)
    assert sorted(test_result) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    test_result = split_integer(3, 5)
    assert test_result == [0, 0, 1, 1, 1]
