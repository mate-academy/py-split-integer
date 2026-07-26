from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)

    assert result == [4, 4, 4, 5]
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_split_on_various_parts_small_values() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(11, 3) == [3, 4, 4]
    assert split_integer(12, 5) == [2, 2, 2, 3, 3]


def test_split_on_various_parts_large_values() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(9, 4) == [2, 2, 2, 3]


def test_distribution_when_remainder_exists() -> None:
    assert split_integer(7, 3) == [2, 2, 3]
    assert split_integer(8, 3) == [2, 3, 3]


def test_only_last_number_is_incremented() -> None:
    assert split_integer(14, 4) == [3, 3, 4, 4]


def test_difference_between_min_and_max_should_be_no_more_than_one() -> None:
    result = split_integer(17, 4)

    assert result == [4, 4, 4, 5]
    assert max(result) - min(result) <= 1


def test_number_of_parts_should_match_requested() -> None:
    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(3, 5)) == 5
