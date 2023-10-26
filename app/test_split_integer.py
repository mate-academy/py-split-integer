from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(23, 4)) == 23


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(18, 6)
    assert min(parts) == max(parts) == 3


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(21, 1) == [21]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(29, 5)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result_with_zero = split_integer(4, 6)
    assert result_with_zero == [0, 0, 1, 1, 1, 1]

