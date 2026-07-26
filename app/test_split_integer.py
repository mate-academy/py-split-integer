from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(6, 2)) == 6


def test_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert all(part == split_integer(6, 2)[0] for part in split_integer(6, 2))


def test_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_sorted_when_not_equal() -> None:
    assert split_integer(1545, 15) == sorted(split_integer(1545, 15))


def test_add_zeros_when_value_less_than_number_of_parts() -> None:
    assert split_integer(4, 5) == [0, 1, 1, 1, 1]
