from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    total = sum(split_integer(32, 6))
    assert total == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(16, 4)
    assert min(result) == max(result)
    assert len(result) == 4


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(32, 1) == [32]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert sorted(result) == result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(4, 6)
    assert result[0] == 0 and result[1] == 0
    assert len(result) == 6


def test_max_min_difference_should_be_less_than_or_equal_to_one() -> None:
    parts = split_integer(17, 4)
    assert (max(parts) - min(parts)) <= 1
