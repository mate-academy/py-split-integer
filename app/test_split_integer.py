from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(35, 35)) == 35


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 3) == [2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(55, 1) == [55]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(37, 4)) == split_integer(37, 4)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 4) == [0, 1, 1, 1]
