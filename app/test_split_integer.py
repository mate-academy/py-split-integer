from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(15, 3)) == 15


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(set(split_integer(15, 3))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(15, 1) == [15]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(16, 5)) == split_integer(16, 5)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 8).count(0) == 8 - 5
