from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 5)
    assert len(result) == 5
    assert all(isinstance(part, int) for part in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(10, 1) == [10]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(10, 4)
    assert result == [2, 2, 3, 3]
    assert len(result) == 4
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 5)
    assert result == [0, 0, 0, 0, 1]
    assert len(result) == 5
    assert max(result) - min(result) <= 1
