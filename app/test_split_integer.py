from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(20, 4)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(set(split_integer(10, 2))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(32, 1) == [32]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 8
    result = split_integer(value, parts)
    assert result.count(0) == parts - value
    assert sum(result) == value

def test_difference_between_min_max_number_in_parts_no_more_one() -> None:
    result = split_integer(27, 4)
    assert max(result) - min(result) <= 1
