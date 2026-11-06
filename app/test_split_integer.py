from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert len(result) == 2
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
    assert result == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert len(result) == 1
    assert max(result) - min(result) <= 1
    assert result == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result1 = split_integer(17, 4)
    assert len(result1) == 4
    assert max(result1) - min(result1) <= 1
    assert result1 == sorted(result1)
    assert result1 == [4, 4, 4, 5]

    result2 = split_integer(32, 6)
    assert len(result2) == 6
    assert max(result2) - min(result2) <= 1
    assert result2 == sorted(result2)
    assert result2 == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 5)
    assert len(result) == 5
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
    assert result == [0, 0, 0, 1, 1]
