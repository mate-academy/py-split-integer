from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)

    result = split_integer(14, 6)
    assert sum(result) == 14
    assert len(result) == 6
    assert all(isinstance(x, int) for x in result)

    result = split_integer(8, 1)
    assert sum(result) == 8
    assert len(result) == 1
    assert all(isinstance(x, int) for x in result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3]
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)

    result = split_integer(15, 3)
    assert result == [5, 5, 5]
    assert len(result) == 3
    assert all(isinstance(x, int) for x in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result == [10]
    assert len(result) == 1
    assert all(isinstance(x, int) for x in result)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert all(isinstance(x, int) for x in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 4
