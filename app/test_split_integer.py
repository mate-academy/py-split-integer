from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(10, 3)) == 10

    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6), (10, 3)]:
        result = split_integer(value, parts)
        assert len(result) == parts
        assert max(result) - min(result) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3]
    assert max(result) - min(result) == 0
    assert len(result) == 2

    result = split_integer(20, 4)
    assert result == [5, 5, 5, 5]
    assert max(result) - min(result) == 0
    assert len(result) == 4


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert result == [8]
    assert len(result) == 1

    result = split_integer(100, 1)
    assert result == [100]
    assert len(result) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 4

    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 6

    result = split_integer(10, 3)
    assert result == [3, 3, 4]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 3


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 3)
    assert result == [0, 1, 1]
    assert sum(result) == 2
    assert len(result) == 3
    assert max(result) - min(result) <= 1
    assert result == sorted(result)

    result = split_integer(1, 4)
    assert result == [0, 0, 0, 1]
    assert sum(result) == 1
    assert len(result) == 4
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
