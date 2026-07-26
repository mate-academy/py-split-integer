from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 8
    parts = 2
    expected_part = value // parts
    assert split_integer(value, parts) == [expected_part] * parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts
    assert sum(result) == value
    assert result == sorted(result)
    assert min(result) == 0


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    result = split_integer(2, 5)
    assert max(result) - min(result) <= 1
