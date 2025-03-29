from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(15, 3)) == 15


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(40, 8) == [5, 5, 5, 5, 5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(11, 3) == sorted(split_integer(11, 3))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]


def test_is_split_integer_length_correct() -> None:
    assert len(split_integer(100, 64)) == 64


def test_when_number_of_parts_zero() -> None:
    assert split_integer(10, 0) == []
