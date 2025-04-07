from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(100, 7)) == 100


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 2) == [5, 5]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(10, 4)
    assert result == sorted(result)
    assert result != [2, 2, 2, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
    assert split_integer(0, 2) == [0, 0]


def test_difference_between_any_parts_should_not_be_more_than_one() -> None:
    result = split_integer(20, 6)
    assert max(result) - min(result) <= 1

    result = split_integer(14, 5)
    assert max(result) - min(result) <= 1

    result = split_integer(100, 9)
    assert max(result) - min(result) <= 1


def test_should_not_return_all_equal_parts_when_remainder_exists() -> None:
    result = split_integer(5, 2)
    assert result != [2, 2]
    assert result == [2, 3]


def test_should_not_increment_only_one_part() -> None:
    result = split_integer(8, 3)
    assert result != [2, 2, 4]
    assert result == [2, 3, 3]


def test_should_handle_large_numbers() -> None:
    value, parts = 1_000_003, 10
    result = split_integer(value, parts)
    assert sum(result) == value
    assert max(result) - min(result) <= 1

    value, parts = 999_997, 11
    result = split_integer(value, parts)
    assert sum(result) == value
    assert max(result) - min(result) <= 1
