from app import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer.split_integer(17, 4)
    assert sum(result) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer.split_integer(8, 4)
    assert result == [2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer.split_integer(8, 1)
    assert result == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer.split_integer(17, 4)
    assert result == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer.split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]


def test_difference_between_max_and_min_should_be_less_or_equal_one() -> None:
    result = split_integer.split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_should_return_exact_number_of_parts() -> None:
    result = split_integer.split_integer(17, 4)
    assert len(result) == 4


def test_should_split_32_into_6_parts_correctly() -> None:
    result = split_integer.split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]


def test_should_split_10_into_3_parts_correctly() -> None:
    result = split_integer.split_integer(10, 3)
    assert result == [3, 3, 4]


def test_should_split_2_into_4_parts_correctly() -> None:
    result = split_integer.split_integer(2, 4)
    assert result == [0, 0, 1, 1]
