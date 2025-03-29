from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 45
    number_of_parts = 7
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(36, 6) == [6, 6, 6, 6, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    expect_res = sorted(result)
    assert result == expect_res


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
