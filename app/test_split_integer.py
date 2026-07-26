from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 4)
    assert sum(result) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(8, 4)
    assert result == [2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(10, 3)
    assert result == [3, 3, 4]


def test_max_min_diff_at_most_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 5)
    assert result == [0, 0, 0, 1, 1]


def test_could_split_on_different_parts() -> None:
    assert split_integer(32, 1) == [32]
    assert split_integer(32, 2) == [16, 16]
    assert split_integer(32, 4) == [8, 8, 8, 8]


def test_only_last_number_is_incremented() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_with_remainder() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
