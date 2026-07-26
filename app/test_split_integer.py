from app.split_integer import split_integer


def test_should_split_value_unevenly() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_split_into_almost_equal_parts() -> None:
    assert split_integer(10, 3) == [3, 3, 4]


def test_sum_of_parts_should_equal_value() -> None:
    assert sum(split_integer(17, 4)) == 17
