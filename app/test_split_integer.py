import app.split_integer as split_integer_module


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer_module.split_integer(17, 4)) == 17
    assert sum(split_integer_module.split_integer(6, 2)) == 6
    assert sum(split_integer_module.split_integer(32, 6)) == 32
    assert sum(split_integer_module.split_integer(3, 5)) == 3
    assert sum(split_integer_module.split_integer(8, 1)) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer_module.split_integer(16, 4) == [4, 4, 4, 4]
    assert split_integer_module.split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer_module.split_integer(8, 1) == [8]
    assert split_integer_module.split_integer(17, 1) == [17]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer_module.split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer_module.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer_module.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer_module.split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer_module.split_integer(1, 3) == [0, 0, 1]
    assert sum(split_integer_module.split_integer(1, 3)) == 1
    assert len(split_integer_module.split_integer(1, 3)) == 3
    assert split_integer_module.split_integer(2, 4) == [0, 0, 1, 1]
    assert sum(split_integer_module.split_integer(2, 4)) == 2
    assert len(split_integer_module.split_integer(2, 4)) == 4
