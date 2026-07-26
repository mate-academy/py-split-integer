from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6), (19, 5), (10, 3)]:
        result = split_integer(value, parts)
        assert sum(result) == value
        assert len(result) == parts
        assert all(isinstance(x, int) for x in result)
        assert result == sorted(result)
        assert max(result) - min(result) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_should_split_uneven_values_correctly() -> None:
    result1 = split_integer(17, 4)
    assert result1 == [4, 4, 4, 5]
    assert len(result1) == 4
    assert all(isinstance(x, int) for x in result1)
    assert result1 == sorted(result1)
    assert max(result1) - min(result1) <= 1

    result2 = split_integer(32, 6)
    assert result2 == [5, 5, 5, 5, 6, 6]
    assert len(result2) == 6
    assert all(isinstance(x, int) for x in result2)
    assert result2 == sorted(result2)
    assert max(result2) - min(result2) <= 1
