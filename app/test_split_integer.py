from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]


def test_difference_between_max_and_min_should_be_not_greater_than_1() -> None:
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1


def test_should_split_value_when_not_divisible() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_split_remainder_between_last_parts() -> None:
    assert split_integer(14, 4) == [3, 3, 4, 4]
