from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(11, 4)) == 11
    assert sum(split_integer(6, 3)) == 6
    assert sum(split_integer(17, 6)) == 17
    assert sum(split_integer(3, 5)) == 3
    assert sum(split_integer(0, 3)) == 0


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 3) == [2, 2, 2]
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(0, 3) == [0, 0, 0]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17]
    assert split_integer(0, 1) == [0]
    assert split_integer(1, 1) == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(11, 4)
    assert result == sorted(result)

    result = split_integer(17, 6)
    assert result == sorted(result)

    result = split_integer(7, 3)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
    assert split_integer(1, 3) == [0, 0, 1]


def test_should_return_empty_list_when_split_into_zero_parts() -> None:
    assert split_integer(5, 0) == []
    assert split_integer(0, 0) == []


def test_remainder_should_be_distributed_evenly() -> None:
    assert split_integer(11, 4) == [2, 3, 3, 3]
    assert split_integer(17, 6) == [2, 3, 3, 3, 3, 3]
    assert split_integer(7, 3) == [2, 2, 3]


def test_should_not_increment_only_last_element() -> None:
    result = split_integer(11, 4)
    assert result.count(3) == 3
    assert result.count(2) == 1
