from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(19, 6)) == 19


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(20, 5).count(4) == 5


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert len(split_integer(15, 1)) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(32, 6)) == sorted([6, 5, 6, 5, 5, 5])


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 4)[0] == 0 and split_integer(3, 4).count(0) == 1
