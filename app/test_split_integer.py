from app import split_integer


def test_sum_of_parts_should_be_equal_to_value() -> None:
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6), (11, 4), (3, 5)]:
        assert sum(split_integer.split_integer(value, parts)) == value


def test_should_return_exactly_number_of_parts_elements() -> None:
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5)]:
        assert len(split_integer.split_integer(value, parts)) == parts


def test_difference_between_max_and_min_should_not_exceed_one() -> None:
    for value, parts in [(17, 4), (32, 6), (11, 4), (10, 7), (3, 5)]:
        result = split_integer.split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_parts_should_be_sorted_ascending() -> None:
    for value, parts in [(17, 4), (32, 6), (11, 4), (10, 7)]:
        result = split_integer.split_integer(value, parts)
        assert result == sorted(result)


def test_should_return_value_itself_when_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_should_split_evenly_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_should_return_ones_when_value_equals_number_of_parts() -> None:
    assert split_integer.split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_return_zeros_and_ones_when_value_less_than_parts() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_distribute_remainder_greater_than_one() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer.split_integer(11, 4) == [2, 3, 3, 3]
    assert split_integer.split_integer(10, 7) == [1, 1, 1, 1, 2, 2, 2]
