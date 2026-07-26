import app.split_integer as split_integer_module


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer_module.split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer_module.split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer_module.split_integer(10, 1) == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer_module.split_integer(10, 3) == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer_module.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_difference_between_parts_is_not_greater_than_one() -> None:
    result = split_integer_module.split_integer(10, 3)
    assert max(result) - min(result) <= 1


def test_number_of_parts_is_correct() -> None:
    assert len(split_integer_module.split_integer(10, 3)) == 3
    assert len(split_integer_module.split_integer(3, 5)) == 5


def test_smaller_parts_go_first() -> None:
    result = split_integer_module.split_integer(10, 3)
    assert result == sorted(result)


def test_sum_when_value_less_than_parts() -> None:
    assert sum(split_integer_module.split_integer(3, 5)) == 3
