from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:

    assert sum(split_integer(18, 4)) == 18


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:

    assert split_integer(9, 3)[0] == split_integer(9, 3)[-1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:

    assert split_integer(8, 1)[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:

    assert split_integer(17, 4)[0] < split_integer(17, 4)[-1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:

    assert split_integer(3, 4)[0] == 0
